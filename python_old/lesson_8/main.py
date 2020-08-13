import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_current_dir
from game import run_game

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Введите название команды')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            if len(sys.argv) == 4:
                text = sys.argv[3]
                create_file(name, text)
            else:
                create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            if len(sys.argv) == 3:
                print('Отсутствует название файла или папки назначения')
            else:
                print('Отсутствует название копируемого файла или папки')
        else:
            copy_file(name, new_name)
    elif command == 'change_dir':
        try:
            path = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            change_current_dir(path)
    elif command == 'fun':
        run_game()
    elif command == 'help':
        print('list - список файлок и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('change_dir - сменить текущую папку')
        print('fun - игра')

save_info('Конец')