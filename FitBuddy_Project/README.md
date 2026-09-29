# FitBuddy – AI Fitness Plan Generator

FitBuddy is a FastAPI + Jinja2 + SQLite web application based on the supplied SmartBridge project document. It accepts a user's name, ID, age, weight, fitness goal, and workout intensity; generates a 7-day plan and nutrition tip; stores the result; and allows feedback-based plan updates.

## Features

- Personalized 7-day workout generation
- Nutrition/recovery tip
- Feedback-based plan revision
- SQLite + SQLAlchemy persistence
- Jinja2 HTML interface
- All-users/admin dashboard
- Delete-user action
- FastAPI Swagger docs at `/docs`
- Built-in fallback mode so the application can be demonstrated without an API key

## Technology

- Python
- FastAPI
- Uvicorn
- Jinja2
- SQLAlchemy + SQLite
- Google Gemini API
- HTML/CSS
- Pydantic

## Run on Windows

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

API documentation: `http://127.0.0.1:8000/docs`

## Gemini setup

Put your Google API key in `.env`:

```env
GOOGLE_API_KEY=your_key_here
```

The supplied project document specifies Gemini 1.5 Pro for workout generation/updates and Gemini Flash for nutrition tips. The model names are configurable through `GEMINI_WORKOUT_MODEL` and `GEMINI_TIP_MODEL`.

If no key is supplied, FitBuddy uses a deterministic demo fallback so the UI and database workflow can still be demonstrated.

## Main routes

- `GET /` – home page
- `POST /generate-workout` – generate and store a plan
- `POST /submit-feedback` – update a plan using feedback
- `GET /view-all-users` – admin view
- `POST /delete-user/{user_id}` – delete a user and plan
- `GET /docs` – FastAPI interactive documentation

## Project structure

```text
FitBuddy_Project/
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── gemini_generator.py
│   ├── gemini_flash_generator.py
│   └── updated_plan.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── result.html
│   ├── all_users.html
│   └── error.html
├── static/
│   ├── style.css
│   └── images/gym.svg
├── docs/
├── tests/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Important project note

This is a student project/demo, not medical advice. Generated exercise and nutrition content should be reviewed by a qualified professional when a user has health conditions, injuries, or other special requirements.
