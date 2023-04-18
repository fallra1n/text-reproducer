import threading
import back.session
import os

from tkinter import filedialog
from back.text_reproducer import run

last_file_path = ''
is_new_file = True


def open_file_dialog() -> None:
    global is_new_file
    global last_file_path
    last_file_path = filedialog.askopenfilename()
    is_new_file = True


def play_text(paused_cv: threading.Condition) -> None:
    if is_new_file:
        if back.session.is_paused:
            back.session.is_running = False
            back.session.mutex.acquire()
            with paused_cv:
                paused_cv.notify_all()

        back.session.mutex.acquire()
        back.session.is_paused = False
        back.session.is_running = True
        t = threading.Thread(target=run, args=(last_file_path, paused_cv))
        t.start()
        back.session.mutex.release()
    else:
        back.session.is_paused = False
        with paused_cv:
            paused_cv.notify_all()


def stop_playing(paused_cv: threading.Condition) -> None:
    back.session.mutex.acquire()
    back.session.is_running = False

    if back.session.is_paused:
        with paused_cv:
            paused_cv.notify_all()


def pause_playing() -> None:
    back.session.is_paused = True
    global is_new_file
    is_new_file = False


def get_path_to_images() -> str:
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    images = os.path.join(parent_dir, 'images/icons')
    return images
