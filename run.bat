@echo off

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not installed or not in PATH.
    pause
    exit /b
) 

: Check if usable conda environment exists
call conda env list | findstr 'transcriber_env'
if %errorlevel% neq 0 (

    echo Conda environment is not set up.
    echo This means the required dependencies are not installed in their respected environment.

    :user_question
    set /p bool_user_in = "Set up conda environment?  Y/N"

    if /i %bool_user_in% == "" (
        echo Please provide a valid argument.
        goto user_question

    ) else if /i %bool_user_in% == "Y" (
        goto is_conda_env_installed

    ) else if /i %bool_user_in% == "N" (
        echo Cannot proceed without functional conda environment.
        echo Terminating...
        echo .
        exit
    )

) else (
    call conda activate transcriber_env
    cd whisper-queuer
    call python main.py

    pause
)

:is_conda_env_installed
conda --version >nul 1>&1
if errorlevel 1 (
    echo Conda is not installed. Please install it first.
    exit /b 1
)

echo Setting up the Conda environment ()...
conda env create -f environment.yml

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