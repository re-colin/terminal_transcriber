import time
from classes import FileEvent
from functions import input_directory
from functions import output_directory
from functions import model_size
from functions import device
from watchdog.observers import Observer

def main():
    print("\nStarting observer...")

    event_handler = FileEvent()
    observer = Observer()
    
    observer.schedule(event_handler, input_directory, recursive=True)
    observer.start()
    print(f"""
        OBSERVER STARTED. ----------------------

        Audio input directory set to    {input_directory}
        Transcription result directory  {output_directory}
        Whisper model                   {model_size}
        Whisper processing device       {device}
        
        Edit these settings in 'settings.json' 
        If new files are detected during runtime, they will be processed.

        Terminate this program with Ctrl+C.

        ----------------------------------------
    """)

    try:
        while True:
            time.sleep(2)

    except KeyboardInterrupt:
        print(f"\nSTOPPING...")
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()