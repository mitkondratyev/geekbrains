# Задание №1
def sentence(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)

print(sentence('Василий', 21, 'Москва'))


# Задание №2

def max_number(num1, num2, num3):
    return max([num1, num2, num3])

print(max_number(-9, 0, 1))


# Задание №3
player = enemy = {
    'name': None,
    'health': 100,
    'damage': 50
}

def attack(player, enemy):
    enemy['health'] -= player['damage']

player['name'] = input('Введите имя атакующего: ')
enemy['name'] = input('Введите имя атакуемого: ')
attack(player, enemy)
print(f'Тукущее здоровье {enemy["name"]} - {enemy["health"]}')



# Задание №4
player1 = enemy1 = {
    'name': None,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

def damage(damage, armor):
    return damage/armor

def attack_with_armor(player, enemy):
    enemy['health'] -= damage(player['damage'], enemy['armor'])

player1['name'] = input('Введите имя атакующего: ')
enemy1['name'] = input('Введите имя атакуемого: ')
attack_with_armor(player1, enemy1)
print(f'Тукущее здоровье {enemy1["name"]} - {enemy1["health"]}')