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
byte_text = pickle.dumps(my_favourite_group)
print(json_text)
print(type(json_text))
print(byte_text)
print(type(byte_text))

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)