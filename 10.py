import numpy as np


numbers = np.sort([int(n) for n in open("10.txt").readlines()])

# part 1
joltages = np.r_[0, numbers, max(numbers) + 3]
counts = np.bincount(np.diff(joltages))
print(counts[1] * counts[3])

# part 2
sol = {0: 1}
for n in numbers:
    sol[n] = sol.get(n - 1, 0) + sol.get(n - 2, 0) + sol.get(n - 3, 0)

print(sol[max(numbers)])
