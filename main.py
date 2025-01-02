# todo
# [] learn 2 use json for user data
# [] format file events properly/move class/add transcription event
# [X] adjust cmp_files (comparing input to output dir)
# [] install ffmpeg
# goodnight

from functions import *
from classes import *

def main():
    print("STARTING main()...")
   
    path = input_directory # USER DIRECTORY HERE

    event_handler = FileEvent()
    observer = Observer()
    
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("OBSERVER STARTED.\n")

    try:
        while True:
            time.sleep(2)

    except KeyboardInterrupt:
        print(f"\nHalting observer...")
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
