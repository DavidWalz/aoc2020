# https://adventofcode.com/2020/day/13
import numpy as np

t, bus = open("13.txt").readlines()
t = int(t)
idx, freq = np.array([[i, int(s)] for i, s in enumerate(bus.split(",")) if s != "x"]).T


# part 1
wait = freq - t % freq
i = np.argmin(wait)
print(wait[i] * freq[i])


# part 2
# brute force solution (too slow)
# t0 = 0
# while not np.all((freq - t0 % freq) % freq == idx):
#     t0 += freq[0]
# print(t0)

# chinese remainder theorem
t0 = np.int64(0)
p = np.int64(1)
for i, f in zip(idx, freq):
    while (t0 + i) % f != 0:
        t0 += p
    p *= f
print(t0)