import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'app'))
sys.path.append(os.path.join(os.getcwd(), 'back'))

import app

# Запуск приложения
if __name__ == "__main__":
    new_app = app.App()
    new_app.run()
