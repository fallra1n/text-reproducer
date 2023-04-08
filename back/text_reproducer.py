import threading

from back.session import Session


def Run(file_path: str, paused_cv: threading.Condition) -> None:
    target = open(file_path, 'r')
    text = target.readlines()

    a = Session()
    a.Play(text, paused_cv)
