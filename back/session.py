import pyttsx3


class Session:
    engine = pyttsx3.Engine

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 100)
        self.engine.setProperty('volume', 0.8)

    def Play(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
