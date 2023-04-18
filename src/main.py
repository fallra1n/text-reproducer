from app import App
import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'app'))
sys.path.append(os.path.join(os.getcwd(), 'back'))


# Запуск приложения
if __name__ == "__main__":
    app = App()
    app.run()
