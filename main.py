from classes import *
from watchdog.observers import Observer
import multiprocessing

def main():
    event_handler = FileEvent()
    observer = Observer()
    
    observer.schedule(event_handler, input_directory, recursive=True)
    observer.start()
    print(f"""
        OBSERVER STARTED. ----------------------

        Audio input directory set to    {input_directory}
        Transcription result directory  {output_directory}
        Whisper model                   {model_type}
        Whisper processing device       {device}
        
        Edit these settings in 'settings.json' 
        If new files are detected, they will be processed.

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
