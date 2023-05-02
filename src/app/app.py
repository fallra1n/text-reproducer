import os
import signal

import tkinter as tk

from PIL import ImageTk, Image

from widgets_handlers import WidgetsHandlers
from widgets_handlers import get_path_to_images


class App:
    win = tk.Tk
    choose_btn = tk.Button
    playing_btn = tk.Button
    stopping_btn = tk.Button
    back_img = Image.Image
    play_img = Image.Image
    stop_img = Image.Image
    pause_img = Image.Image
    file_label = tk.Label
    handlers = WidgetsHandlers()

    def __init__(self):
        self.win = tk.Tk()

    def init_title(self) -> None:
        self.win.title('Text Reproducer')

    def set_geometry(self) -> None:
        self.win.geometry('1120x700+500+300')
        self.win.maxsize(1120, 700)

    def choosing_btn_init(self) -> None:
        self.choose_btn = tk.Button(
            self.win,
            text="Выбрать файл",
            command=lambda: self.handlers.open_file_dialog(self.file_label))
        self.choose_btn.config(width=11, height=1)
        self.choose_btn.place(x=10, y=220)

    def playing_btn_init(self) -> None:
        # play image
        self.play_img = Image.open(
            get_path_to_images() + '/play.jpg')
        resized_image = self.play_img.resize((100, 100))
        self.play_img = ImageTk.PhotoImage(resized_image)

        # pause image
        self.pause_img = Image.open(
            get_path_to_images() + '/pause.png')
        resized_image = self.pause_img.resize((100, 100))
        self.pause_img = ImageTk.PhotoImage(resized_image)

        self.playing_btn = tk.Button(
            self.win,
            command=lambda: self.handlers.play_text(
                self.play_img, self.pause_img, self.playing_btn),
            image=self.play_img,
            bd=0)
        self.playing_btn.place(x=10, y=250)

    def stopping_btn_init(self) -> None:
        self.stop_img = Image.open(
            get_path_to_images() + '/stop.png')
        resized_image = self.stop_img.resize((100, 100))
        self.stop_img = ImageTk.PhotoImage(resized_image)

        self.stopping_btn = tk.Button(
            self.win,
            command=lambda: self.handlers.stop_playing(
                self.play_img, self.pause_img, self.playing_btn, self.file_label),
            image=self.stop_img,
            bd=0)
        self.stopping_btn.place(x=10, y=350)

    def set_background(self) -> None:
        self.back_img = Image.open(
            get_path_to_images() + '/back.jpg')
        resized_image = self.back_img.resize((1120, 700))
        self.back_img = ImageTk.PhotoImage(resized_image)
        label = tk.Label(self.win, image=self.back_img)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def file_label_init(self):
        self.file_label = tk.Label(self.win, text="", font=("Arial", 26))
        self.file_label.pack()
        self.file_label.place(x=200, y=300)

    def run(self) -> None:
        self.set_background()
        self.init_title()
        self.set_geometry()
        self.choosing_btn_init()
        self.playing_btn_init()
        self.stopping_btn_init()
        self.file_label_init()
        self.win.mainloop()

        # Если была пауза, а после остановка(приложения), нам нужно завершить
        # процесс
        if self.handlers.last_process_pid != -1:
            os.kill(self.handlers.last_process_pid, signal.SIGKILL)
