profit = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержки: '))

proceeds = profit - costs


if proceeds > 0:
    print('Вы работает в прибыль')
    # Прибыль / выручка * 100 % = рентабельность выручки
    print('Рентабельность выручки ', proceeds/profit*100)
    staff = int(input('Введите количество сотрудников: '))
    print('Прибыль фирмы на одного сотрудника ', proceeds / staff)
else:
    print('Вы работает в убыток')