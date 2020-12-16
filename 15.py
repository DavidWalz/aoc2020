# https://adventofcode.com/2020/day/15
from tqdm import tqdm

numbers = [6, 4, 12, 1, 20, 0, 16]


def say_nth(nth):
    last_seen = {n: i for i, n in enumerate(numbers[:-1])}
    next = numbers[-1]
    i0 = len(numbers) - 1
    for i in tqdm(range(i0, nth - 1)):
        n = next
        if n in last_seen:
            next = i - last_seen[n]
        else:
            next = 0
        last_seen[n] = i
    print(next)


# part 1
say_nth(2020)

# part 2
say_nth(30000000)