# whisper-queuer
A Python script for Whisper batch processing that runs in the terminal.
This project was created as a personal tool, so it still has a handful of issues and quirks.

## Setting up / Requirements
Clone this repository either by downloading a ZIP or cloning it using git:

~~~ shell
git clone https://github.com/re-colin/terminal_transcriber.git
~~~

Since this uses conda software, and doesn't add conda to your user PATH by default, the default Command Prompt program won't recognize it if you double-click on `run.bat`. A temporary workaround is to use the Anaconda Prompt and run it from there:

~~~ shell 
cd terminal_transcriber
run
~~~

The only other manual installation requirement is Miniconda from https://docs.anaconda.com/miniconda/install/. This application can't function without it.

## Usage / How it works
Run `run.bat`. A conda environment should be set up for you automatically so you can use it relatively out-of-the-box.

This application uses `watchdog` observers to monitor a file directory with the audio files you want to transcribe. If it detects a new file, it will go ahead and begin the process of transcribing it using Whisper, and toss the result into an output directory.

Settings such as which directories it decides to use can be specified inside `settings.json`. 

Note that the input directory is by default set to /audio_samples/, output is set to ~/Outputs/, and the default model size is `small`, all defined within `functions.py`. 
`"device"` refers to whether or not Whisper should transcribe using the CPU/Cuda, etc. I believe that as of writing this Whisper tends to default to the CPU.

~~~ json
{
   "path_to_input_directory": "",
   "path_to_output_directory": "",
   "model": "",
   "device": ""
}
~~~
