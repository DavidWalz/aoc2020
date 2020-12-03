# https://adventofcode.com/2020/day/3
import numpy as np

lines = open("3.txt").read().split("\n")
A = np.array([[c == "#" for c in line] for line in lines], dtype=int)

ny, nx = A.shape


def count_trees(dx, dy=1):
    iy = np.arange(0, ny, dy)
    ix = (np.arange(len(iy)) * dx) % nx
    return sum(A[iy, ix])


# part 1
print(count_trees(3))

# part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = [count_trees(dx, dy) for dx, dy in slopes]
print(np.prod(trees))
