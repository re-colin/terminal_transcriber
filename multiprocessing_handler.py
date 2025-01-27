import multiprocessing
import threading

# Manage max thread/process count
# Add setting to settings.json

def handle_multi_process(func, args):
    new_process = multiprocessing.Process(target=func, args=(args,))

    new_process.start()

    new_process.join()


def handle_multi_thread(func, args):
    new_thread = threading.Thread(target=func, args=(args,))

    new_thread.start()

    new_thread.join()

