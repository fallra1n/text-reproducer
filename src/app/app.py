import threading
import tkinter as tk

from widgets_handlers import open_file_dialog, play_text, stop_playing, get_path_to_images, pause_playing
from PIL import ImageTk, Image

import back.session


class App:
    win = tk.Tk
    choose_btn = tk.Button
    playing_btn = tk.Button
    stopping_btn = tk.Button
    pause_btn = tk.Button
    back_img = Image.Image
    play_img = Image.Image
    stop_img = Image.Image
    pause_img = Image.Image
    paused_cv = threading.Condition

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
            command=open_file_dialog)
        self.choose_btn.config(width=41, height=1)
        self.choose_btn.place(x=400, y=220)

    def playing_btn_init(self) -> None:
        self.play_img = Image.open(get_path_to_images() + '/play.jpg')
        resized_image = self.play_img.resize((100, 100))
        self.play_img = ImageTk.PhotoImage(resized_image)

        self.playing_btn = tk.Button(
            self.win,
            command=lambda: play_text(self.paused_cv),
            image=self.play_img,
            bd=0)
        self.playing_btn.place(x=400, y=250)

    def stopping_btn_init(self) -> None:
        self.stop_img = Image.open(get_path_to_images() + '/stop.png')
        resized_image = self.stop_img.resize((100, 100))
        self.stop_img = ImageTk.PhotoImage(resized_image)

        self.stopping_btn = tk.Button(
            self.win,
            command=lambda: stop_playing(self.paused_cv),
            image=self.stop_img,
            bd=0)
        self.stopping_btn.place(x=610, y=250)

    def pause_btn_init(self) -> None:
        self.pause_img = Image.open(get_path_to_images() + '/pause.png')
        resized_image = self.pause_img.resize((100, 100))
        self.pause_img = ImageTk.PhotoImage(resized_image)

        self.pause_btn = tk.Button(
            self.win,
            command=pause_playing,
            image=self.pause_img,
            bd=0)
        self.pause_btn.place(x=505, y=250)

    def set_background(self) -> None:
        self.back_img = Image.open(get_path_to_images() + '/back.jpg')
        resized_image = self.back_img.resize((1120, 700))
        self.back_img = ImageTk.PhotoImage(resized_image)
        label = tk.Label(self.win, image=self.back_img)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def init_cv(self) -> None:
        self.paused_cv = threading.Condition()

    def run(self) -> None:
        self.set_background()
        self.init_title()
        self.set_geometry()
        self.choosing_btn_init()
        self.playing_btn_init()
        self.stopping_btn_init()
        self.pause_btn_init()
        self.init_cv()
        self.win.mainloop()

        # Если была пауза, а после остановка(приложения), нам нужно завершить
        # поток
        if back.session.is_paused:
            back.session.mutex.acquire()
            back.session.is_running = False

            if back.session.is_paused:
                with self.paused_cv:
                    self.paused_cv.notify_all()
