import multiprocessing
import os
import signal
import tkinter as tk

from tkinter import filedialog
from PIL import Image

from back.text_reproducer import run


class WidgetsHandlers:
    last_file_path = ''
    last_process_pid = -1
    is_new_file = False
    is_playing = True
    is_stopped = True

    def open_file_dialog(self, file_label: tk.Label) -> None:

        self.last_file_path = filedialog.askopenfilename()
        self.is_new_file = True
        self.is_stopped = False

        file_name = self.last_file_path.split("/")[-1]
        file_label.config(text=file_name)

    def play_text(self, play_img: Image.Image, pause_img: Image.Image,
                  btn: tk.Button) -> None:
        if self.is_new_file:
            # если последний процесс еще не убит
            if self.last_process_pid != -1:
                os.kill(self.last_process_pid, signal.SIGKILL)

            new_process = multiprocessing.Process(
                target=run, args=(self.last_file_path, ))
            new_process.start()
            self.last_process_pid = new_process.pid
        elif self.last_process_pid != -1:
            os.kill(self.last_process_pid, signal.SIGCONT)

        if not self.is_stopped:
            btn.configure(image=pause_img)
            btn.configure(command=lambda: self.pause_playing(play_img, pause_img, btn))
            self.is_playing = True

    def stop_playing(self, play_img: Image.Image, pause_img: Image.Image,
                     btn: tk.Button, file_label: tk.Label) -> None:
        self.is_new_file = False

        if self.last_process_pid != -1:
            os.kill(self.last_process_pid, signal.SIGKILL)
        self.last_process_pid = -1

        self.is_stopped = True

        if self.is_playing:
            btn.configure(image=play_img)
            btn.configure(command=lambda: self.play_text(play_img, pause_img, btn))
            self.is_playing = False

        file_label.config(text="")

    def pause_playing(self, play_img: Image.Image, pause_img: Image.Image,
                      btn: tk.Button) -> None:
        self.is_new_file = False
        if self.last_process_pid != -1:
            os.kill(self.last_process_pid, signal.SIGSTOP)

        btn.configure(image=play_img)
        btn.configure(command=lambda: self.play_text(play_img, pause_img, btn))
        self.is_playing = False


def get_path_to_images() -> str:
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    images = os.path.join(parent_dir, 'images/icons')
    return images
