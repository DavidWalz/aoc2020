import numpy as np
from scipy.ndimage.filters import convolve


lines = open("17.txt").read().split("\n")
M = np.array([[c == "#" for c in line] for line in lines]).astype(int)


def bootup(dims=3):
    A = M.copy()

    for _ in range(dims - 2):
        A = A[..., np.newaxis]

    # 3^dims kernel with 0 in the middle
    kernel = np.ones((3,) * dims)
    np.put(kernel, kernel.size // 2, 0)

    for _ in range(6):
        # pad with zeros on each side
        A = np.pad(A, ((1, 1),) * dims, mode="constant", constant_values=0)

        # count number of active neighbors
        neighbors = convolve(A, kernel, mode="constant", cval=0)

        # cycle
        to_inactive = (A == 1) & ((neighbors < 2) | (neighbors > 3))
        to_active = (A == 0) & (neighbors == 3)
        A[to_inactive] = 0
        A[to_active] = 1

    print(np.sum(A))


# part 1
bootup(3)

# part 2
bootup(4)