# https://adventofcode.com/2020/day/2
import numpy as np
from itertools import combinations

A = np.genfromtxt("1.txt")


def foo(r):
    return [np.prod(a) for a in combinations(A, r) if sum(a) == 2020]


# part 1
print(foo(2))

# part 2
print(foo(3))
