import whisper
import time
import os
import json
import sys

models = [
    "small",
    "medium",
    "large"
]

cwd = os.getcwd()
model_type = models[0]
input_directory = f"{cwd}/audio_samples/"
output_directory = os.path.expanduser("~/Outputs/")


def write_to_output(result, output):
    if os.path.exists(output_directory) == False:
        os.mkdir(output_directory)

    with open(f"{output}/{result}.md") as output_file:
        output_file.write(result)


def cmp_file_directory_contents(file):
    in_output = False

    if os.path.exists(f"{output_directory}{file}"):
        in_output = True
    
    return in_output 


def transcribe_start(file):
    start = time.time()
    model = whisper.load_model(name = model_type)

    print(f"Model selected: {model_type}")
    print(f"TRANSCRIBING...")

    audio = whisper.load_audio(file)
    # Below line throws a FileNotFoundError
    # assuming its related to ffmpeg-python not being installed
    # there should be no problem with how the audio sample is being referenced
    result = model.transcribe(audio)
    
    print("\nTRANSCRIPTION COMPLETE: \n")
    print(result['text'])

    result_file_name_full = f"{file}.md"

    write_to_output(result_file_name_full, output_directory)

    end = time.time()
    total_time = end - start
    print(f"TRANSCRIPTION TIME: {total_time} secs using {model_type} model.")
