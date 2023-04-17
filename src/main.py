import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'app'))
sys.path.append(os.path.join(os.getcwd(), 'back'))

from app import App

# Запуск приложения
if __name__ == "__main__":
    app = App()
    app.run()
