@echo off

:: install usable version of python here if user answers Y
:: possibly seperate said scripts for when they're required in main.py
:: carry out conda forging of modules

:is_conda_installed
conda --version >nul 2>&1
if errorlevel 1 (
    echo Conda is not installed. Please install it first.
    exit /b 1
)
:eof


echo Setting up the Conda environment...
conda env create -f environment.yml

if errorlevel 1 (
    echo Failed to create the environment. Check your environment.yml file.
    exit /b 1
)

REM Activate the environment
echo Activating the environment...
call conda activate environment 

if errorlevel 1 (
    echo Failed to activate environment. Ensure Conda is properly set up in your shell.
    exit /b 1
)

echo Environment setup complete.
 