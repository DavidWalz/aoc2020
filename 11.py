# https://adventofcode.com/2020/day/11
import numpy as np
from scipy.signal import convolve2d


lines = open("11_test.txt").read().split("\n")
seats = np.array([[c == "L" for c in line] for line in lines])


# part 1
occupied = np.zeros_like(seats)
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

while True:
    # empty seats with only empty adjacents seats become filled
    come = seats & ~occupied & (convolve2d(occupied, kernel, "same") == 0)

    # filled seats with 4+ filled adjacents seats become empty
    leave = seats & occupied & (convolve2d(occupied, kernel, "same") >= 4)

    # apply changes
    occupied[come] = 1
    occupied[leave] = 0

    if come.sum() + leave.sum() == 0:
        break

print(occupied.sum())


# part 2
