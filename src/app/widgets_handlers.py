import multiprocessing
import os
import signal
import tkinter as tk

from tkinter import filedialog
from PIL import Image

from back.text_reproducer import run

last_file_path = ''
last_process_pid = -1
is_new_file = False
is_playing = True
is_stopped = True


def open_file_dialog(file_label: tk.Label) -> None:
    global is_new_file
    global last_file_path
    global is_stopped

    last_file_path = filedialog.askopenfilename()
    is_new_file = True
    is_stopped = False

    file_name = last_file_path.split("/")[-1]
    file_label.config(text=file_name)


def play_text(play_img: Image.Image, pause_img: Image.Image,
              btn: tk.Button) -> None:
    if is_new_file:
        # если последний процесс еще не убит
        global last_process_pid
        if last_process_pid != -1:
            os.kill(last_process_pid, signal.SIGKILL)

        new_process = multiprocessing.Process(
            target=run, args=(last_file_path, ))
        new_process.start()
        last_process_pid = new_process.pid
    elif last_process_pid != -1:
        os.kill(last_process_pid, signal.SIGCONT)

    if not is_stopped:
        btn.configure(image=pause_img)
        btn.configure(command=lambda: pause_playing(play_img, pause_img, btn))
        global is_playing
        is_playing = True


def stop_playing(play_img: Image.Image, pause_img: Image.Image,
                 btn: tk.Button, file_label: tk.Label) -> None:
    global is_new_file
    is_new_file = False

    global last_process_pid
    if last_process_pid != -1:
        os.kill(last_process_pid, signal.SIGKILL)
    last_process_pid = -1

    global is_stopped
    is_stopped = True

    global is_playing
    if is_playing:
        btn.configure(image=play_img)
        btn.configure(command=lambda: play_text(play_img, pause_img, btn))
        is_playing = False

    file_label.config(text="")


def pause_playing(play_img: Image.Image, pause_img: Image.Image,
                  btn: tk.Button) -> None:
    global is_new_file
    is_new_file = False
    if last_process_pid != -1:
        os.kill(last_process_pid, signal.SIGSTOP)

    btn.configure(image=play_img)
    btn.configure(command=lambda: play_text(play_img, pause_img, btn))
    global is_playing
    is_playing = False


def get_path_to_images() -> str:
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    images = os.path.join(parent_dir, 'images/icons')
    return images
