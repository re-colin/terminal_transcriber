import whisper
import time
import os
import json
import sys

cwd = os.getcwd()
input_directory = f"{cwd}/audio_samples/"
output_directory = os.path.expanduser("~/default_out/")

models = [
    "small",
    "medium",
    "large"
]


def write_to_output(result, output):
    with open(f"{output}/{result}.md") as output_file:
        output_file.write(result)


def cmp_file_directory_contents(file):
    in_output = False

    if os.path.exists(f"{output_directory}{file}"):
        in_output = True
    
    return in_output 


def transcribe_start(file, model_sel):
    start = time.time()
    model = whisper.load_model(name = models[model_sel])

    print(f"Model selected: {models[model_sel]}")
    print(f"TRANSCRIBING...")

    audio = whisper.load_audio(file)
    # Below line throws a FileNotFoundError
    # assuming its related to ffmpeg-python not being installed
    # there should be no problem with how the audio sample is being referenced
    result = model.transcribe(audio)
    
    print("\nTRANSCRIPTION COMPLETE: \n")
    print(result['text'])

    result_file_format = f"{file}.md"

    write_to_output(result_file_format, output_directory)

    end = time.time()
    total_time = end - start
    print(f'TRANSCRIPTION TIME: {total_time} secs. ')
