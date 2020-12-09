# https://adventofcode.com/2020/day/9
from itertools import combinations


numbers = [int(n) for n in open("9.txt").readlines()]


# part 1
def check(i):
    n = numbers[i]
    prev = numbers[i - 25 : i]
    return any([s == n for s in map(sum, combinations(prev, 2))])


for i in range(25, len(numbers)):
    if not check(i):
        invalid = numbers[i]
        print(invalid)
        break


# part 2
weaknesses = []
for i in range(len(numbers)):
    s = numbers[i]
    for j in range(i + 1, len(numbers)):
        s += numbers[j]
        if s == invalid:
            # weakness found
            w = numbers[i:j]
            print(min(w) + max(w))
        if s >= invalid:
            break
