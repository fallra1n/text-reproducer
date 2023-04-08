from app.apl import App
import sys
import os

# добавим в os.path директорию на один уровень выше текущей,
# чтобы можно было найти модули из директории back
sys.path.append(os.path.join(os.getcwd(), '..'))

# Запуск приложения
if __name__ == "__main__":
    app = App()
    app.Run()
