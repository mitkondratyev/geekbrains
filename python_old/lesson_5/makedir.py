import sys, os

def get_path(i):
    return os.path.join(os.getcwd(), 'dir_{}'.format(i))

def make_dirs():
    for i in range(1, 10):
        path = get_path(i)
        if not os.path.isdir(path):
            os.mkdir(path)

def remove_dirs():
    for i in range(1, 10):
        path = get_path(i)
        if os.path.isdir(path):
            os.rmdir(path)

def check_dirs(function, message):
    all_dirs_checked = True
    for i in range(1, 10):
        path = get_path(i)
        if function(path):
            print(message.format(path))
            all_dirs_checked = False
    return all_dirs_checked

def unit_test():
    before_creation_folders = os.listdir()
    print('Файлы до создания папок ', before_creation_folders)
    make_dirs()
    if check_dirs(lambda path: not os.path.isdir(path), 'Папка {} не была создана'):
        print('Все папки были созданы')
    after_creation_folders = os.listdir()
    print('Файлы после создания папок ', after_creation_folders)
    remove_dirs()
    if check_dirs(lambda path: os.path.isdir(path), 'Папка {} не была удалена'):
        print('Все папки были удалены')
    after_remove_folders = os.listdir()
    print('Файлы после удаления папок ', after_remove_folders)

if __name__ == '__main__':
    unit_test()