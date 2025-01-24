@echo off
echo Calling run.bat...
setlocal enabledelayedexpansion

call C:/Users/%USERNAME%/miniconda3/Scripts/activate.bat
if errorlevel 1 (
    call C:/Users/%USERNAME%/Anaconda3/Scripts/activate.bat    
    if errorlevel 1 (
        echo Cannot use conda from the current command prompt.
        echo Use the Anaconda Prompt or add your conda installation to PATH.
    )
)




:: echo Errorlevel after conda --version: %errorlevel%
call conda --version
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
    goto activate_conda_env
)

del temp_env_list.txt

:setup_conda_env

echo Setting up Conda environment...
call conda env create -f environment.yml

if errorlevel 1 (
    echo Failed to create conda environment. Check your environment.yml file.
    exit /b 1
)

echo Environment setup complete.

:activate_conda_env
echo Activating environment...

call conda activate transcriber_env

if errorlevel 1 (
    echo Failed to activate environment. Ensure Conda is properly set up in your shell.
    exit /b 1
)

cd terminal_transcriber
call python main.py