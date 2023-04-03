import tkinter as tk
import threading


from tkinter import filedialog
from back.text_reproducer import Run
import back.session

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


def run_app():
    win = tk.Tk()
    win.title('Text Reproducer')
    win.geometry('1120x700+500+300')

    btn_choose_file = tk.Button(
        win,
        text="Выбрать файл",
        command=open_file_dialog)
    btn_choose_file.pack()

    btn_play_text = tk.Button(win, text="Проиграть", command=play_text)
    btn_play_text.pack()

    btn_stop_playing = tk.Button(
        win,
        text="Остановить проигрование",
        command=stop_playing)
    btn_stop_playing.pack()

    win.mainloop()


if __name__ == "__main__":
    run_app()
