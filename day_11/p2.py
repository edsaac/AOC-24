from itertools import chain
from functools import cache
import matplotlib.pyplot as plt

stone_dict = {0: 0}


@cache
def blink(n: int):
    if n == 0:
        return (1,)

    elif len(str(n)) % 2 == 0:
        n_digits = len(str(n))
        left, right = str(n)[: n_digits // 2], str(n)[n_digits // 2 :]
        return (int(left), int(right))

    else:
        return (n * 2024,)


@cache
def blink_25_times(stone: int):
    after_stones = [stone]

    for i in range(25):
        after_stones = list(chain.from_iterable([blink(n) for n in after_stones]))

    stone_dict.update({stone: len(after_stones)})

    return len(after_stones)


list_of_stones = [0]

for stone in list_of_stones:
    print(blink_25_times(stone))
