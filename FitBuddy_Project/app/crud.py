from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import User, Plan


def save_user(db: Session, data):
    user = db.scalar(select(User).where(User.user_id == data.user_id))
    if user:
        user.name = data.name
        user.age = data.age
        user.weight = data.weight
        user.goal = data.goal
        user.intensity = data.intensity
    else:
        user = User(
            user_id=data.user_id,
            name=data.name,
            age=data.age,
            weight=data.weight,
            goal=data.goal,
            intensity=data.intensity,
        )
        db.add(user)
    db.commit()
    db.refresh(user)
    return user


def save_plan(db: Session, user_id: str, original_plan: str, nutrition_tip: str):
    plan = db.scalar(select(Plan).where(Plan.user_id == user_id))
    if not plan:
        plan = Plan(
            user_id=user_id,
            original_plan=original_plan,
            nutrition_tip=nutrition_tip,
        )
        db.add(plan)
    else:
        plan.original_plan = original_plan
        plan.nutrition_tip = nutrition_tip
        plan.updated_plan = None
        plan.feedback = None
        plan.updated_at = None
    db.commit()
    db.refresh(plan)
    return plan


def get_user(db: Session, user_id: str):
    return db.scalar(select(User).where(User.user_id == user_id))


def get_plan(db: Session, user_id: str):
    return db.scalar(select(Plan).where(Plan.user_id == user_id))


def update_plan(db: Session, plan: Plan, revised_plan: str, feedback: str):
    plan.updated_plan = revised_plan
    plan.feedback = feedback
    plan.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(plan)
    return plan


def get_all_users(db: Session):
    return db.scalars(select(User).order_by(User.id.desc())).all()


def get_all_plans(db: Session):
    return db.scalars(select(Plan)).all()


def delete_user(db: Session, user_id: str):
    user = get_user(db, user_id)
    plan = get_plan(db, user_id)
    if plan:
        db.delete(plan)
    if user:
        db.delete(user)
    db.commit()
    return bool(user)
