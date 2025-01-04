@echo off

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not installed or not in PATH.
    pause
    exit /b
) 

if exist requirements.txt (
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install some dependencies.
        pause
    )
)

for /f "tokens=2 delims= " %%i in ('python --version') do set py_version=%%i

echo Python %py_version% detected. Running main.py...
python main.py

pause