import random

unfair_coin_probability = random.random()


def unbiased_random():
    while True:
        x = _biased_random()
        y = _biased_random()
        if x != y:
            break
    return x


def _biased_random():
    return 1 if random.random() <= unfair_coin_probability else 0
