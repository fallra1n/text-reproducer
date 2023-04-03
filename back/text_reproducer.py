from back.session import Session


def Run(file_path):
    target = open(file_path, 'r')
    text = target.readlines()

    a = Session()
    a.Play(text)


if __name__ == '__main__':
    raise Exception("неправильное использование библиотеки")
