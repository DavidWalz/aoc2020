# https://adventofcode.com/2020/day/5
# Row and column numbers can be recovered from the binary partitioning by replacing
# the characters F/R to 0 and B/L to 1 and reading the code in base 2.
import numpy as np

lines = open("5.txt").read().split("\n")


def seat(line):
    for r in (("F", "0"), ("B", "1"), ("R", "1"), ("L", "0")):
        line = line.replace(*r)
    row = int(line[:7], 2)
    col = int(line[7:], 2)
    return [row, col]

def seatID(row, col):
    return row * 8 + col

rows, cols = np.array(list(map(seat, lines))).T

# part 1: find maximum seat ID
print(max(seatID(rows, cols)))

# part2: find the empty seat with non-empty seats next to it
A = np.zeros((128, 8), bool)
A[rows, cols] = 1
B = ~A & np.roll(A, 1, axis=0) & np.roll(A, -1, 0) & np.roll(A, 1, 1) & np.roll(A, -1, 1)
print(seatID(*np.where(B)))