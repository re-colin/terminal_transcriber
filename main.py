import whisper
import time
import os
import json
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


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


def cmp_files(file_path):
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

class FileEvent(LoggingEventHandler):
    # TODO
    # get source path for corresponding action performed on file
    # compare to output directory
    # perform action based on its action type

    def on_modified(self, event):
        print("ugghhh")
        print(f"{event.event_type}")
        print(f"{event.src_path}")

    def on_created(self, event):
        print("SHIT")
        print(f"{event.event_type}")
        print(f"{event.src_path}")

    def on_deleted(self, event):
        print("im so tired its 22:35")

def main():
    cwd = os.getcwd()
    file = f"/Bots Bridges and Euler Circuits.mp4"
    
    input = f"{cwd}{file}"
    print(input)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    event_handler = LoggingEventHandler()
    file_handler = FileEvent()
    observer = Observer()
    
    observer.schedule(file_handler, path, recursive=True)

    observer.start()
    
    try:
        while True:
            time.sleep(2)
    
    except KeyboardInterrupt:
        print(f"\nHalting observer...")
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
