import random

def get_rand(list):
    result = None
    if len(list) > 0:
        result = random.choice(list)
    return result

if __name__ == '__main__':
    print(get_rand([1, 2, 3, 4]))