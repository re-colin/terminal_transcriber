import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from functions import cmp_file_directory_contents

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

        if cmp_file_directory_contents(created_file_name) == False:
            print("Enact transcription here!!!!!")
        else:
            print("This file exists, apparently!")

