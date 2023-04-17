import pyttsx3
import threading

is_running = True
is_paused = False
mutex = threading.Lock()


class Session:
    engine = pyttsx3.Engine

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 120)
        self.engine.setProperty('volume', 1.0)

    def play(self, text: list, paused_cv: threading.Condition) -> None:
        for string in text:
            words = string.split()

            for word in words:
                if is_paused:
                    with paused_cv:
                        paused_cv.wait()

                if not is_running:
                    mutex.release()
                    return

                self.engine.say(word)
                self.engine.runAndWait()
