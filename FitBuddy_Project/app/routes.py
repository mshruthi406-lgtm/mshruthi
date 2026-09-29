from pathlib import Path
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import UserInput, FeedbackRequest
from app.crud import (
    delete_user, get_all_plans, get_all_users, get_plan, get_user,
    save_plan, save_user, update_plan,
)
from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash
from app.updated_plan import update_workout_plan

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def render(request: Request, template_name: str, context: dict, status_code: int = 200):
    return templates.TemplateResponse(
        request=request,
        name=template_name,
        context=context,
        status_code=status_code,
    )


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return render(request, "index.html", {"request": request})


@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    name: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    db: Session = Depends(get_db),
):
    data = UserInput(
        name=name.strip(),
        user_id=user_id.strip(),
        age=age,
        weight=weight,
        goal=goal.strip(),
        intensity=intensity,
    )
    user = save_user(db, data)

    workout_plan = generate_workout_gemini(
        user.name, user.age, user.weight, user.goal, user.intensity
    )
    nutrition_tip = generate_nutrition_tip_with_flash(user.goal)
    plan = save_plan(db, user.user_id, workout_plan, nutrition_tip)

    return render(
        request,
        "result.html",
        {
            "request": request,
            "user": user,
            "plan": plan,
            "workout_plan": plan.updated_plan or plan.original_plan,
            "nutrition_tip": plan.nutrition_tip,
            "message": None,
        },
    )


@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...),
    db: Session = Depends(get_db),
):
    data = FeedbackRequest(
        user_id=user_id.strip(),
        feedback=feedback.strip(),
    )

    user = get_user(db, data.user_id)
    plan = get_plan(db, data.user_id)

    if not user or not plan:
        return render(
            request,
            "error.html",
            {
                "request": request,
                "message": "User ID not found. Generate a plan first.",
            },
            status_code=404,
        )

    revised = update_workout_plan(
        plan.original_plan,
        data.feedback,
        user.goal,
        user.intensity,
    )

    plan = update_plan(
        db,
        plan,
        revised,
        data.feedback,
    )

    return render(
        request,
        "result.html",
        {
            "request": request,
            "user": user,
            "plan": plan,
            "workout_plan": revised,
            "nutrition_tip": plan.nutrition_tip,
            "message": "Your plan has been updated based on your feedback!",
        },
    )


@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request, db: Session = Depends(get_db)):
    users = get_all_users(db)
    plans = {p.user_id: p for p in get_all_plans(db)}

    return render(
        request,
        "all_users.html",
        {
            "request": request,
            "users": users,
            "plans": plans,
        },
    )


@router.post("/delete-user/{user_id}")
def remove_user(user_id: str, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return RedirectResponse(
        url="/view-all-users",
        status_code=303,
    )
