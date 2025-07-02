# Ensure compatibility between different shells (zsh vs bash)
# !#usr/bin/bash

# Create conda env
# Ensure conda is only initialized within this program's dedicated shell instance
# rather than user-wide
# MacOS -> https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
# Linux -> https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# If conda not found in default location
# echo "conda not found in [conda default loc]
# echo "would you like to install conda now?" yes|no

# if yes
# install conda from respective platform

# if environment doesnt exist, create it

# then -
# activate environment
# call main.py in project directory
