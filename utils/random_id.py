from random import randint


def get_random_id() -> int:
    random_id = randint(10000, 99999)
    return random_id