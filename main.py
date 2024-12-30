import whisper
import time
import os

default_directory = ""
transcripton_queue = []

models = [
    "small",
    "medium",
    "large"
]

def transcribe_start(file, default_directory):
    start = time.time()
    model = whisper.load_model(name = models[0])

    result = model.transcribe(file)
    
    print("\nTRANSCRIPTION COMPLETE: \n")
    print(result['text'])

    with open(default_directory, 'w') as f:
        f.write(result['text'])

    end = time.time()
    total_time = end - start
    print(f'TRANSCRIPTION RUNTIME: {total_time} secs. ')


def main():
    pass

if __name__ == "__main__":
    main()