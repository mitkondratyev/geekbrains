a = int(input('Введите результат первого дня спортсмена: '))
b = int(input('Введите желаемый результат: '))

day = 1
current = a


while current < b:
    current = current+current*0.1
    day = day + 1
print(day)