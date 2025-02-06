@echo off

conda list | findstr "torch" 
if errorlevel 1 (
    :: install here
)

conda list | findstr "torchvision"
if errorlevel 1 (
    :: install here
    call conda install torchvision -c nvidia
)

conda list | findstr "torchaudio"
if errorlevel 1 (
    :: install here
)