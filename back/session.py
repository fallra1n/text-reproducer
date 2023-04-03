import pyttsx3

is_running = True


class Session:
    engine = pyttsx3.Engine

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 100)
        self.engine.setProperty('volume', 0.8)

    def Play(self, text):
        text_without = ''.join([char for char in text if char != 'f'])

        words = text_without.split()
        for word in words:
            if not is_running:
                break

            self.engine.say(word)
            self.engine.runAndWait()
