import os, shutil, datetime

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка уже существует')

def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        try:
            os.remove(name)
        except FileNotFoundError:
            print('Файл для удаления не найден')

def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка уже существует')
    else:
        try:
            shutil.copy(name, new_name)
        except FileNotFoundError:
            print('Файл для копирования не найден')

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

def change_current_dir(path):
    if os.path.isdir(path):
        try:
            print(os.getcwd())
            os.chdir(path)
            print(os.getcwd())
        except FileNotFoundError:
            print('Папка не найдена')
    else:
        print('Параметром должна быть папка, а не файл')


if __name__ == '__main__':
    create_file('test_create_file.txt')
    create_folder('test_create_folder')
    get_list()

    copy_file('test_create_file.txt', 'test_create_file_copy.txt')
    copy_file('test_create_folder', 'test_create_folder_copy')
    get_list()

    delete_file('test_create_file.txt')
    delete_file('test_create_folder')
    delete_file('test_create_file_copy.txt')
    delete_file('test_create_folder_copy')
    get_list()
