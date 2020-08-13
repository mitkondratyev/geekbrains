import math

#1
def function1(fruits1, fruits2):
    result = []
    try:
        result = [fruit for fruit in fruits1 if fruit in fruits2]
    except Exception as e:
        print('Ошибка:', e)
    return result


#2
def function2(numbers):
    result = []
    try:
        result = [number for number in numbers if number%3 == 0 and number > 0 and number%4 != 0]
    except Exception as e:
        print('Ошибка:', e)
    return result

#3
def function3(number_list):
    result = []
    try:
        result = [number if number <= 0 else math.sqrt(number) for number in number_list]
    except Exception as e:
        print('Ошибка:', e)
    return result

#4
def function4(number):
    try:
        number = int(number)
        if number == 13:
            raise ValueError("Нельзя вводить 13")
        result = number**2
    except Exception as e:
        print('Ошибка:', e)
    else:
        return result

fruits1 = ['яблоко', 'груша', 'лайм', 'фейхоа']
fruits2 = ['хурма', 'груша', 'лайм', 'папайя', 'айва']
print(function1(fruits1, fruits2))

numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
print(function2(numbers))

print(function3(numbers))

number = input('Введите число:')
print(function4(number))