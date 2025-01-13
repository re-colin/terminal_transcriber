@echo off
echo Calling run.bat...
setlocal enabledelayedexpansion

:: echo Errorlevel after conda --version: %errorlevel%
if errorlevel 1 (
    echo Conda is not installed. Please install it first at
    echo https://docs.anaconda.com/miniconda/install/.
    exit /b 1
) else (
    echo Conda detected.
)

:: echo Checking for Conda environment...
call conda env list > temp_env_list.txt
findstr "transcriber_env" temp_env_list.txt >nul

if errorlevel 1 (
    goto setup_conda_env

) else (
    echo Conda environment found. Running main.py...
    call conda activate transcriber_env
    cd whisper-queuer
    call python main.py
)

:setup_conda_env

del temp_env_list.txt

echo Setting up Conda environment...
call conda env create -f environment.yml

if errorlevel 1 (
    echo Failed to create conda environment. Check your environment.yml file.
    exit /b 1
)

echo Activating environment...

call conda activate transcriber_env

if errorlevel 1 (
    echo Failed to activate environment. Ensure Conda is properly set up in your shell.
    exit /b 1
)

echo Environment setup complete.