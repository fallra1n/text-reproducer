import pyttsx3


class Session:
    engine: pyttsx3.Engine

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 100)
        self.engine.setProperty('volume', 1.0)

    def play(self, text: list) -> None:
        for string in text:
            self.engine.say(string)
            self.engine.runAndWait()
