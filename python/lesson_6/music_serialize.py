import pickle, json

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [
        {'name': 'Делать панк-рок','year': 2016},
        {'name': 'Шапито','year': 2014}
    ]
}
json_text = json.dumps(my_favourite_group)
byte_text = json_text.encode('utf-8')
print(json_text)
print(type(json_text))
print(byte_text)
print(type(byte_text))

with open('group.json', 'w', encoding='utf-8') as f:
    f.write(json_text)

with open('group.pickle', 'wb') as f:
    f.write(byte_text)