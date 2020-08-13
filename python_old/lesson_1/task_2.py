
while True:
    number = int(input('Please input number: '))
    if number > 0 and number < 10:
        print(number**2)
        break
    else:
        print('Number should be more than 0 and less than 10')