import numpy as np


images = {}  # tile id -> image
tile2edge = {}  # tile id -> edge hashes
edge2tile = {}  # edge hash -> tile ids having that edge

def hashit(arr):
    # edges can be flipped. take the lower of both hashess.
    h1 = hash(arr.tobytes())
    h2 = hash(arr[::-1].tobytes())
    return min(h1, h2)

for i, tile in enumerate(open("20.txt").read().split("\n\n")):
    key, image = tile.split(":\n")
    key = int(key.strip("Tile "))
    image = np.array([[c == "#" for c in row] for row in image.split("\n")])
    images[key] = image
    for edge in ([image[0], image[-1], image[:, 0], image[:, -1]]):
        h = hashit(edge)
        tile2edge.setdefault(key, []).append(h)
        edge2tile.setdefault(h, []).append(key)


# part 1: product of ids of corner tiles (tiles with 2 unmatched edges)
unmatched = {}
for h, tiles in edge2tile.items():
    assert len(tiles) <= 2
    if len(tiles) == 2:  # more than one tile with this edge
        continue
    tile = tiles[0]
    unmatched[tile] = unmatched.get(tile, 0) + 1

corners = [k for k, v in unmatched.items() if v == 2]
print(np.array(corners, dtype=np.int64).prod())


# part 2: build up the image and count #'s that are not sea monsters
def get_neighbors(t, exclude):
    neighbors = []
    for edge in tile2edge[t]:
        neighbors += edge2tile[edge]
    return list(filter(lambda x: x not in exclude, neighbors))

def is_neighbor(t1, t2):
    for edge in tile2edge[t1]:
        if t2 in edge2tile[edge]:
            return True
    return False


# Arrange the tiles. We go from left to right and top to bottom and place the 1-2
# neighboring tiles (right and bottom) we haven't yet considered.
# When placing the bottom tile we check if it's edge matches that of its left neighbor.
n = int(len(images) ** 0.5)
A = np.zeros((n, n), dtype=int)
A[0, 0] = corners[0]
for iy in range(n - 1):
    for ix in range(n - 1):
        tiles = get_neighbors(A[iy, ix], exclude=A)
        if len(tiles) == 1:  # once we get to the second row the right neighbors are already placed
            A[iy + 1, ix] = tiles[0]
            continue
        t1, t2 = tiles
        if ix > 1:  # check if lower tile shares an edge with its left neighbor
            if is_neighbor(t1, A[iy + 1, ix - 1]):
                t1, t2 = t2, t1
        A[iy, ix + 1] = t1
        A[iy + 1, ix] = t2
A[-1, -1] = next(filter(lambda x: x not in A, corners))  # remaining corner

# All tiles are now in the correct position
# TODO:
# - flip & rotate the individual tiles to match their edges
# - crop all edges
# - filter all occurences of sea monsters
# - count remaining #'s