import pickle, json

with open('group.json', 'r', encoding='utf-8') as f:
    my_favourite_group = json.load(f)

print(my_favourite_group)
print(type(my_favourite_group))

with open('group.pickle', 'rb') as f:
    bytes = f.read()
    my_favourite_group = json.loads(bytes)

print(my_favourite_group)
print(type(my_favourite_group))