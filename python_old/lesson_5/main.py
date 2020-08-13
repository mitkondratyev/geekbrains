import makedir, sys, os
from list import get_rand

def test_modules():
    print('Тест 1 модуля')
    before_creation_folders = os.listdir()
    print('Файлы до создания папок ', before_creation_folders)
    makedir.make_dirs()
    if makedir.check_dirs(lambda path: not os.path.isdir(path), 'Папка {} не была создана'):
        print('Все папки были созданы')
    after_creation_folders = os.listdir()
    print('Файлы после создания папок ', after_creation_folders)
    makedir.remove_dirs()
    if makedir.check_dirs(lambda path: os.path.isdir(path), 'Папка {} не была удалена'):
        print('Все папки были удалены')
    after_remove_folders = os.listdir()
    print('Файлы после удаления папок ', after_remove_folders)

    print('Тест 2 модуля')
    print('Случайное число - ', get_rand([1, 2, 3, 4]))

test_modules()