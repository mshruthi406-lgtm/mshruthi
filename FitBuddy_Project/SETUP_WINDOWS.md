# FitBuddy Windows Setup

Open Command Prompt in the FitBuddy project folder.

## 1. Create virtual environment

```cmd
python -m venv .venv
```

## 2. Install dependencies

```cmd
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 3. Start the application

```cmd
.venv\Scripts\python.exe run.py
```

Or double-click `start.bat`.

## 4. Open the website

http://127.0.0.1:8000

## 5. API documentation

http://127.0.0.1:8000/docs

## 6. Optional Gemini API key

Copy `.env.example` to `.env`:

```cmd
copy .env.example .env
```

Then edit `.env` and put your Google API key in:

```env
GOOGLE_API_KEY=YOUR_KEY_HERE
```

The application can still be demonstrated without a key because it contains a local fallback generator.

## Common error fixed

If you see:

```text
TypeError: cannot use 'tuple' as a dict key
```

make sure the project's `app/routes.py` is the version included in this package. It uses the current Starlette-compatible form:

```python
templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"request": request},
)
```
