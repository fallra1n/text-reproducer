import sys
import os

# добавим в os.path директорию на один уровень выше текущей,
# чтобы можно было найти модули из директории back
sys.path.append(os.path.join(os.getcwd(), '..'))

from app.app import App

# Запуск приложения
if __name__ == "__main__":
    app = App()
    app.Run()
