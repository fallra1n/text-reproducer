import multiprocessing
import os
import signal

from tkinter import filedialog

from back.text_reproducer import run

last_file_path = ''
last_process_pid = -1
is_new_file = True


def open_file_dialog() -> None:
    global is_new_file
    global last_file_path
    last_file_path = filedialog.askopenfilename()
    is_new_file = True


def play_text() -> None:
    if is_new_file:
        # если последний процесс еще не убит
        global last_process_pid
        if last_process_pid != -1:
            os.kill(last_process_pid, signal.SIGKILL)

        new_process = multiprocessing.Process(target=run, args=(last_file_path, ))
        new_process.start()
        last_process_pid = new_process.pid
    else:
        os.kill(last_process_pid, signal.SIGCONT)


def stop_playing() -> None:
    global last_process_pid
    if last_process_pid != -1:
        os.kill(last_process_pid, signal.SIGKILL)
    last_process_pid = -1


def pause_playing() -> None:
    global is_new_file
    is_new_file = False
    if last_process_pid != -1:
        os.kill(last_process_pid, signal.SIGSTOP)


def get_path_to_images() -> str:
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    images = os.path.join(parent_dir, 'images/icons')
    return images
