@echo off
echo Calling run.bat...
setlocal enabledelayedexpansion

:: conda --version >nul 2>&1
echo Errorlevel after conda --version: %errorlevel%
if errorlevel 1 (
    echo Conda is not installed. Please install it first.
    echo See https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html.
    exit /b 1
) else (
    echo Conda detected. Continuing...
)

echo Checking for Conda environment...
call conda env list > temp_env_list.txt
findstr "transcriber_env" temp_env_list.txt >nul
:start
if errorlevel 1 (
    echo Conda environment is not set up.
    echo This means the required dependencies are not installed in their respected environment.

    set /p bool_user_in="Set up conda environment?  y/n   "

    if /i "%bool_user_in%"=="" (
        echo Please provide a valid argument.
        goto start
    )
    if /i "%bool_user_in%"=="y" (
        goto setup_conda_env
    ) 
    if /i "%bool_user_in%"=="n" (
        echo Cannot proceed without functional conda environment.
        echo Terminating...
        echo .
        exit
    )

) else (
    del temp_env_list.txt
    echo Conda environment found.
    call "%CONDA_PREFIX%\condabin\conda.bat" activate transcriber_env
    cd whisper-queuer
    call python main.py

    pause
)

:setup_conda_env
echo Setting up the Conda environment...
call conda env create -f environment.yml

if errorlevel 1 (
    echo Failed to create the environment. Check your environment.yml file.
    exit /b 1
)

echo Activating environment...
call conda activate transcriber_env

if errorlevel 1 (
    echo Failed to activate environment. Ensure Conda is properly set up in your shell.
    exit /b 1
)

echo Environment setup complete.