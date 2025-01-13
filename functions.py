import whisper
import time
import os
import json

with open("settings.json", 'r') as file:
    settings = json.load(file)

input_directory_setting = settings["path_to_input_directory"]
output_directory_setting = settings["path_to_output_directory"]
model_type_setting = settings["model"]
device_setting = settings["device"] 

cwd = os.getcwd() ## Location of this file 

if input_directory_setting == "":         
    input_directory = f"{cwd}/audio_samples/" 

if output_directory_setting == "":
    output_directory = os.path.expanduser("~/Outputs/") 

if model_type_setting == "":
    model_type = "small"

if device_setting == "":
    device = "cpu"

def create_output_file(result, output, output_file_name):
    if os.path.exists(output_directory) == False:
        os.mkdir(output_directory)

    with open(f"{output}/{output_file_name}", "w") as output_file:
        output_file.write(result['text'])


def does_output_exist(file):
    in_output = False

    if os.path.exists(f"{output_directory}{file}"):
        in_output = True
    
    return in_output 


def transcribe_start(file):
    start = time.time()
    model = whisper.load_model(name = model_type)

    print(f"Model selected: {model_type}")

    audio = whisper.load_audio(file)
    print(f"FILE AUDIO LOADED.")

    result = model.transcribe(audio, device=device)
    
    print("\nTRANSCRIPTION COMPLETE: \n")
    print(result['text'])

    file_name = file.split('/')[-1].split('.')[0]
    file_name_output = f"{file_name}.md"

    create_output_file(result, output_directory, file_name_output)

    end = time.time()
    total_time = end - start
    print(f"TRANSCRIPTION TIME: {total_time} secs using {model_type} model.")
