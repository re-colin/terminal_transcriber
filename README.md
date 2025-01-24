# whisper-queuer
A Python script for Whisper batch processing that runs in the terminal.
This project was created as a personal tool, so it still has a handful of issues and quirks.

## Setting up / Requirements
Clone this repository either by downloading a ZIP or cloning it using git:

~~~ shell
git clone https://github.com/re-colin/terminal_transcriber.git
~~~

The only other manual installation requirement is Miniconda3 (or Anaconda3) from https://docs.anaconda.com/miniconda/install/. This application can't function without it.

## Usage / How it works
Run `run.bat`, either by clicking on it or running it from a command prompt. A conda environment should be set up for you automatically so you can use it relatively out-of-the-box.

This application uses `watchdog` observers to monitor a file directory with the audio files you want to transcribe. If it detects a new file, it will go ahead and begin the process of transcribing it using Whisper, and toss the result into an output directory.

Settings such as which directories it decides to use can be specified inside `settings.json`. Default values are as follows. If input and output directories aren't specified, `functions.py` will use `~/terminal_transcriber/audio_samples` and `~/Outputs/` by default respectively.

~~~ json
{
   "path_to_input_directory": "%USER_PATH_HERE%/terminal_transcriber/audio_samples/",
   "path_to_output_directory": "%USER_PATH_HERE%/Outputs/",
   "model": "small",
   "device": "cpu"
}
~~~
