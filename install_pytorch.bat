@echo off

echo Installing Pytorch...

call pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
if errorlevel 1 (
    echo Error installing Pytorch.
    exit /b 1
)
