import os
import json
import random
import string
import time


def random_number(a, b):
    return random.randint(a, b)


def random_username():
    n = random_number(10, 32)
    return ''.join([random.choice(string.ascii_letters) for _ in range(n)])


def random_call_duration():
    return random_number(1000, 3600000)


def random_sample():
    if os.path.isfile('sample.json'):
        print('samples load from sample.json')
        with open('sample.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    users = set()
    cnt = random_number(10, 50)
    while cnt > 0:
        username = random_username()
        if username not in users:
            users.add(username)
            cnt -= 1
    samples = []
    for u in users:
        total_calls = random_number(1, 100)
        print(f'user {u}: random call duration')
        for _ in range(total_calls):
            samples.append({
                'call_duration': random_call_duration(),
                'username': u
            })
    with open('sample.json', 'w', encoding='utf-8') as f:
        json.dump(samples, f, indent=4)
    return samples


if __name__ == '__main__':
    random_sample()
