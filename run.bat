@echo off

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not installed or not in PATH.
    pause
    exit /b
) 

call python main.py

pause