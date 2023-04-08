from app.apl import App
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))


if __name__ == "__main__":
    app = App()
    app.Run()
