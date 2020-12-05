# https://adventofcode.com/2020/day/5
# The seat ID can be recovered from the binary partitioning by replacing
# the characters F/R to 0 and B/L to 1 and reading the code in base 2.
import numpy as np

lines = open("5.txt").read().split("\n")


def seatID(line):
    for r in (("F", "0"), ("B", "1"), ("R", "1"), ("L", "0")):
        line = line.replace(*r)
    return int(line, 2)


ids = np.array(list(map(seatID, lines)))

# part 1: find maximum seat ID
print(max(ids))

# part 2: find the one empty seat with only non-empty seats next to it
A = np.zeros((128, 8), bool)
A[ids // 8, ids % 8] = 1
B = ~A & np.roll(A, 1, 0) & np.roll(A, -1, 0) & np.roll(A, 1, 1) & np.roll(A, -1, 1)
row, col = np.where(B)
print(row * 8 + col)
