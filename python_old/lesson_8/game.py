import random

def run_game():
    print('Здравствуйте, я попытаюсь угадать ваше число.')
    print('Вводите > если ваше число больше.')
    print('Вводите < если ваше число меньше.')
    print('Вводите = если я угадал.')
    input('Загадайте любое число от 1 до 100 и нажмите enter')

    min = 1
    max = 100
    user_answer = None
    clear_range = False

    while user_answer != '=':
        number = random.randint(min, max)
        user_answer = input(f'Ваше число {number}?')
        if user_answer == '>':
            if number == 100:
                print('Загаданное число не может быть больше 100')
                clear_range = True
            min = number + 1
        elif user_answer == '<':
            if number == 1:
                print('Загаданное число не может быть меньше 1')
                clear_range = True
            max = number - 1
        if max < min or min > max or clear_range:
            print('Давайте попробуем заново, загадайте любое число от 1 до 100')
            min = 1
            max = 100
            clear_range = False

    print('Ура, у меня получилось!')


