import tkinter as tk

from app.widgets_handlers import open_file_dialog, play_text, stop_playing, get_path_to_images
from PIL import ImageTk, Image


class App:
    win = tk.Tk
    choose_btn = tk.Button
    playing_btn = tk.Button
    stopping_btn = tk.Button
    back_img = Image.Image
    play_img = Image.Image
    stop_img = Image.Image

    def __init__(self):
        self.win = tk.Tk()

    def initTitle(self):
        self.win.title('Text Reproducer')

    def setGeometry(self):
        self.win.geometry('1120x700+500+300')
        self.win.maxsize(1120, 700)

    def choosingBtnInit(self):
        self.choose_btn = tk.Button(
            self.win,
            text="Выбрать файл",
            command=open_file_dialog)
        self.choose_btn.config(width=26, height=1)
        self.choose_btn.place(x=400, y=220)

    def playingBtnInit(self):
        self.play_img = Image.open(get_path_to_images() + '/play.jpg')
        resized_image = self.play_img.resize((100, 100))
        self.play_img = ImageTk.PhotoImage(resized_image)

        self.playing_btn = tk.Button(
            self.win,
            command=play_text,
            image=self.play_img,
            bd=0)
        self.playing_btn.place(x=400, y=250)

    def stoppingBtnInit(self):
        self.stop_img = Image.open(get_path_to_images() + '/stop.png')
        resized_image = self.stop_img.resize((100, 100))
        self.stop_img = ImageTk.PhotoImage(resized_image)

        self.stopping_btn = tk.Button(
            self.win,
            command=stop_playing,
            image=self.stop_img,
            bd=0)
        self.stopping_btn.place(x=505, y=250)

    def setBackground(self):
        self.back_img = Image.open(get_path_to_images() + '/back.jpg')
        resized_image = self.back_img.resize((1120, 700))
        self.back_img = ImageTk.PhotoImage(resized_image)
        label = tk.Label(self.win, image=self.back_img)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def Run(self):
        self.setBackground()
        self.initTitle()
        self.setGeometry()
        self.choosingBtnInit()
        self.playingBtnInit()
        self.stoppingBtnInit()
        self.win.mainloop()
