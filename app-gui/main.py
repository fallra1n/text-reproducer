import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))

from app.apl import App


if __name__ == "__main__":
    app = App()
    app.Run()
