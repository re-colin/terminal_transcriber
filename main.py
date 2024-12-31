import whisper
import time
import os

print("colin had a syncing conflict this is a test")

default_directory = ""
transcripton_queue = []

models = [
    "small",
    "medium",
    "large"
]

def transcribe_start(file, model_select):
    start = time.time()
    model = whisper.load_model(name = models[model_select])

    print(f"Model selected: {models[model_select]}")
    print(f"TRANSCRIBING...")

    result = model.transcribe(file)
    
    print("\nTRANSCRIPTION COMPLETE: \n")
    print(result['text'])

    with open(default_directory, 'w') as f:
        f.write(result['text'])

    end = time.time()
    total_time = end - start
    print(f'TRANSCRIPTION RUNTIME: {total_time} secs. ')


def main():
    cwd = os.getcwd()
    cwd = "C:/Users/Mark Boda/whisper-queuer"
    file = f"/audio_samples/Bots Bridges and Euler Circuits.mp4"
    input = f"{cwd}{file}"

    print(input)

    transcribe_start(input, 0)

if __name__ == "__main__":
    main()
