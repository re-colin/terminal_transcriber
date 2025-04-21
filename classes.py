import logging
from watchdog.events import FileSystemEventHandler
from functions import does_output_exist
from functions import transcribe_start
import multiprocessing

class FileEvent(FileSystemEventHandler):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    def on_any_event(self, event):
        logging.info(
            f"FILE {event.event_type.upper()}   {event.src_path}"
        )

    def on_created(self, event):
        
        print(event.src_path)

        src = event.src_path
        created_file_name = src.split("/")[-1]
        print(f"Name of new file: {created_file_name}")

        if does_output_exist(created_file_name) == False:

            print(f"\nTRANSCRIBING {src}...\n")

            new_transcribe_process = multiprocessing.Process(target=transcribe_start, args=(src, ))

            new_transcribe_process.start()

            print(f"NEW TRANSCRIPTION PROCESS CREATED - Process ID: {new_transcribe_process.pid}")

            new_transcribe_process.join() # wait for previous job to complete

        else:
            print(f"\nFile {created_file_name} already exists.")

