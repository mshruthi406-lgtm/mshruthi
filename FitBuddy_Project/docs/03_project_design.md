# Phase 3 – Project Design

## Architecture

```text
Browser
   |
   v
Jinja2 HTML Templates
   |
   v
FastAPI Routes
   |
   +----> Gemini workout generation/update
   |
   +----> Gemini nutrition tip
   |
   v
SQLAlchemy ORM
   |
   v
SQLite Database
```

## Main Components
- `main.py`: application creation and static-file mounting.
- `routes.py`: HTTP routes and orchestration.
- `schemas.py`: Pydantic validation.
- `gemini_generator.py`: workout generation.
- `gemini_flash_generator.py`: nutrition/recovery tip.
- `updated_plan.py`: feedback-based revision.
- `crud.py`: database operations.
- `models.py`: SQLAlchemy entities.
- `database.py`: database connection.
- `templates/`: Jinja2 UI.
- `static/`: CSS and image asset.

## Data Model
### User
`id, user_id, name, age, weight, goal, intensity, created_at`

### Plan
`id, user_id, original_plan, updated_plan, nutrition_tip, feedback, updated_at, created_at`

## UI Design
The supplied screenshots/project document use a fitness-oriented interface with a centered input form, a personalized result page, feedback form, and all-users table. This implementation follows that same flow with a responsive card/table layout.
