import whisper
import time
import os
import json

input_directory = ""
output_directory = ""
transcripton_queue = []

models = [
    "small",
    "medium",
    "large"
]

def write_to_output(result, output):
    with open(f"{output}/{result}.md") as output_file:
        output_file.write(result)


def create_queue():
    pass


def check_queue():
    exists = False

    for file in (os.listdir(input_directory)):
        if file in os.listdir(output_directory):
            exists = True
            transcripton_queue.remove(file)
            return 1
        
    return -1 



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

    write_to_output(result, output_directory)

    end = time.time()
    total_time = end - start
    print(f'TRANSCRIPTION RUNTIME: {total_time} secs. ')


def main():
    cwd = os.getcwd()
    file = f"/Bots Bridges and Euler Circuits.mp4"
    
    input = f"{cwd}{file}"

    print(input)

    if check_queue() == -1:
        pass

    transcribe_start(file, 0)

if __name__ == "__main__":
    main()
