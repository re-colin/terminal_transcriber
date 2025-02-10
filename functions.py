import whisper
import time
import os
import json
import torch

with open("settings.json", 'r') as file:
    settings = json.load(file)

input_directory = settings["path_to_input_directory"]
output_directory = settings["path_to_output_directory"]
model_size = settings["model"]
device = settings["device"]
# this setting will be for later
# max_processes_allowed = settings["maximum_parallel_processes_allowed"]

cwd = os.getcwd() ## Location of this file 

if os.path.exists(output_directory) == False:
    output_directory = os.path.expanduser("~/Outputs/")

if os.path.exists(input_directory) == False:         
    input_directory = f"{cwd}/audio_samples/" 

if model_size == "":
    model_size = "small"

# Removed device 'blank' check option, since Whisper will terminate anyway if the passed in device param isn't valid
if device == "cuda":
    if torch.cuda.is_available() == False:
        print("""\n
        WARNING: torch.cuda.is_available() evaluates to FALSE.
        This means Pytorch may not be installed inside this environment (transcriber_env).
        Execute the 'install_pytorch.bat' script before trying again, or installing it here manually.
        
        Defaulting to CPU.
        """)
        
        device = "cpu"
        
        
def create_output_file(result, output, output_file_name):
    if os.path.exists(output_directory) == False:
        os.mkdir(output_directory)

    with open(f"{output}/{output_file_name}", "w") as output_file:
        output_file.write(result['text'])


# idk why this is still here
def does_output_exist(file):
    in_output = False

    if os.path.exists(f"{output_directory}{file}"):
        in_output = True
    
    return in_output 


def transcribe_start(file):
    start = time.time()
    
    model = whisper.load_model(name=model_size, device=device)

    print(f"Model selected: {model_size}")

    audio = whisper.load_audio(file)
    print(f"FILE AUDIO LOADED.")
    print(f"TRANSCRIBING...")

    result = model.transcribe(audio)
    
    print("\nTRANSCRIPTION COMPLETE: \n")
    print(result['text'])

    file_name = file.split('/')[-1].split('.')[0]
    file_name_output = f"{file_name}.md"

    create_output_file(result, output_directory, file_name_output)

    end = time.time()
    total_time = end - start
    print(f"\nTRANSCRIPTION TIME: {total_time} secs using {model_size} model.")

