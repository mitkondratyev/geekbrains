number = input('Введите число: ')
max = 0

for i in range(0, len(number)):
    current = int(number[i])
    if max < current:
        max = current

print(max)