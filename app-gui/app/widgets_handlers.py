import threading
import back.session
import os

from tkinter import filedialog
from back.text_reproducer import Run

last_file_path = ''


def open_file_dialog():
    global last_file_path
    last_file_path = filedialog.askopenfilename()


def play_text():
    back.session.is_running = True
    t = threading.Thread(target=Run, args=(last_file_path,))
    t.start()


def stop_playing():
    back.session.is_running = False


def get_path_to_images() -> str:
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    images = os.path.join(parent_dir, 'images')
    return images
