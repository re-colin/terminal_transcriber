import whisper
import time
import os
import json

input_directory = ""
output_directory = ""

models = [
    "small",
    "medium",
    "large"
]

def write_to_output(result, output):
    with open(f"{output}/{result}.md") as output_file:
        output_file.write(result)


def cmp_queue(file_path):
    in_output = False

    file = os.path.basename(file_path).rsplit('.', 1)[0] # extract name of file for comparison to output file

    if file in os.listdir(output_directory):
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


def main():
    cwd = os.getcwd()
    file = f"/Bots Bridges and Euler Circuits.mp4"
    
    input = f"{cwd}{file}"
    print(input)

    # compare directories
    # if input[i] result (based on file title) exists in output already, continue
    # else, transcribe and write to output
    # use watchdog to monitor system.
    # this code doesn't work how i intended it, its just a way of expressing my previous ideas.
    input_state = os.listdir(input_directory)

    for file in input_state: 
        if cmp_queue(file) == False:
            transcribe_start(file)
        else:
            continue

        if os.listdir(input_directory).length() > input_state.length():
            # does this resume????
            # if not try append i guess
            input_state = os.listdir(input_directory)




if __name__ == "__main__":
    main()
