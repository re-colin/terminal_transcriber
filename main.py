from classes import *
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

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
