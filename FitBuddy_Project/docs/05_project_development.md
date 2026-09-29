# Phase 5 – Project Development

## Implemented Backend
FastAPI routes:
- `GET /`
- `POST /generate-workout`
- `POST /submit-feedback`
- `GET /view-all-users`
- `POST /delete-user/{user_id}`

## AI Layer
Workout generation and plan updates are isolated from route logic. Nutrition tips use a separate module. A built-in fallback is included so the complete application can be demonstrated without an active API key.

## Database
SQLAlchemy maps `User` and `Plan` models to SQLite.

## Frontend
Jinja2 templates provide:
- Home/input page
- Result page
- Feedback flow
- All-users dashboard
- Error page

## Security/Configuration
The API key is read from `GOOGLE_API_KEY` and `.env` is ignored by Git.

## Development Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
