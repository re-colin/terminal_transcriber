@echo off

echo Ensuring activation of virtual environment...

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
    del temp_env_list.txt
    echo Virtual environment is not set up.
    echo Run 'run.bat' before attempting to run this script.
    exit /b 1
)

:: Activate virtual environment

call conda activate transcriber_env

if errorlevel 1 (
    echo Failed to activate environment. Ensure Conda is properly set up in your shell.
    exit /b 1
)

del temp_env_list.txt
echo Installing Pytorch...

call pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
if errorlevel 1 (
    echo Error installing Pytorch.
    exit /b 1
)
