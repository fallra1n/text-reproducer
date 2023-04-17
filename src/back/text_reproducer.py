import threading

from back.session import Session


def run(file_path: str, paused_cv: threading.Condition) -> None:
    target = open(file_path, 'r')
    text = target.readlines()

    next_session = Session()
    next_session.play(text, paused_cv)
