import random

unfair_coin_probability = random.uniform(0, 1)


def unbiased_random():
    while True:
        x = _biased_random()
        y = _biased_random()
        if x != y:
            break
    return x


def _biased_random():
    return 1 if random.uniform(0, 1) <= unfair_coin_probability else 0
