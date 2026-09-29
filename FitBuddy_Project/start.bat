@echo off
title FitBuddy - AI Fitness Plan Generator
echo ==========================================
echo        FitBuddy - Starting Server
echo ==========================================
echo.
if not exist ".venv\Scripts\python.exe" (
    echo ERROR: .venv was not found.
    echo Create it with:
    echo   python -m venv .venv
    echo   .venv\Scripts\python.exe -m pip install -r requirements.txt
    pause
    exit /b 1
)
.venv\Scripts\python.exe run.py
pause
