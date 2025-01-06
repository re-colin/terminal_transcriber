import whisper
import time
import os
import json
import sys

models = [
    "small",    # 0
    "medium",   # 1
    "large"     # 2
]

cwd = os.getcwd() ## Location of this file 
model_type = models[0] ## Select model here. Use zero based indexing.
input_directory = f"{cwd}/audio_samples/" ## Default directory where to-be-transcribed audio is located.
output_directory = os.path.expanduser("~/Outputs/") ## Default output directory for transcription results


def write_to_output(result, output, output_file_name):
    if os.path.exists(output_directory) == False:
        os.mkdir(output_directory)

    with open(f"{output}/{output_file_name}.md") as output_file:
        output_file.write(result)


def does_output_exist(file):
    in_output = False

    if os.path.exists(f"{output_directory}{file}"):
        in_output = True
    
    return in_output 


def transcribe_start(file):
    start = time.time()
    model = whisper.load_model(name = model_type)

    print(f"Model selected: {model_type}")

    print(f"\nTRANSCRIBING {file}...\n")
    audio = whisper.load_audio(file)
    print(f"FILE AUDIO LOADED.")

    result = model.transcribe(audio)
    
    print("\nTRANSCRIPTION COMPLETE: \n")
    print(result['text'])

    result_file_name_full = f"{file}.md"
    file_name = result_file_name_full.split('')[0].split() ## Change this.

    write_to_output(output_directory, result_file_name_full, )

    end = time.time()
    total_time = end - start
    print(f"TRANSCRIPTION TIME: {total_time} secs using {model_type} model.")
