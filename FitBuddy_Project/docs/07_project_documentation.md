# Phase 7 – Project Documentation

## Project Title
FitBuddy – AI Fitness Plan Generator using Gemini Models

## Abstract
FitBuddy is a web-based AI application that generates personalized 7-day workout plans and nutrition/recovery tips from basic fitness information. It also provides a feedback loop that revises an existing plan.

## Technology Stack
- Python
- FastAPI
- Jinja2
- SQLAlchemy
- SQLite
- Google Gemini
- HTML/CSS
- Uvicorn

## User Flow
1. Open FitBuddy.
2. Enter profile information.
3. Click Generate Plan.
4. Review user information, workout plan and nutrition tip.
5. Submit feedback.
6. Review updated plan.
7. Administrators can inspect records from All Users.

## Deployment
Local:
```bash
uvicorn app.main:app --reload
```

## API
Swagger:
`/docs`

## Limitations
- The supplied brief describes a local deployment workflow.
- Authentication/authorization is not implemented in this student version.
- Model IDs may need to be changed in `.env` if the AI account exposes different Gemini model names.
- Generated fitness guidance should be reviewed appropriately for individual health circumstances.
