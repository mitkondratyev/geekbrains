inputValue = int(input('Введите секунды: '))
m, s = divmod(inputValue, 60)
h, m = divmod(m, 60)
print("%02d:%02d:%02d" % (h, m, s))