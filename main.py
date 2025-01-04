from classes import *
from watchdog.observers import Observer

def main():
    path = input_directory # USER DIRECTORY HERE

    event_handler = FileEvent()
    observer = Observer()
    
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("\nOBSERVER STARTED.")
    print(f"""
        Default user directory set to {input_directory}.
        Default Whisper model set to {model_type}.
        Edit these settings in 'functions.py'. 

        If new files are detected, they will be processed.
    """)

    try:
        while True:
            time.sleep(2)

    except KeyboardInterrupt:
        print(f"\nHalting program...")
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
