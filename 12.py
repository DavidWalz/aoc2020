# https://adventofcode.com/2020/day/12

navigation = [(line[0], int(line[1:].strip())) for line in open("12.txt").readlines()]

dirs = {"N": 1j, "S": -1j, "E": 1, "W": -1}
turn = {"L": 1j, "R": -1j}


# part 1
pos = 0 + 0j
dir = 1 + 0j

for cmd, val in navigation:
    if cmd in dirs:
        pos += val * dirs[cmd]
    elif cmd in turn:
        dir *= turn[cmd] ** (val // 90)
    elif cmd == "F":
        pos += val * dir

print(abs(pos.real) + abs(pos.imag))


# part 2
pos = 0 + 0j
wp = 10 + 1j

for cmd, val in navigation:
    if cmd in dirs:
        wp += val * dirs[cmd]
    elif cmd in turn:
        wp *= turn[cmd] ** (val // 90)
    elif cmd == "F":
        pos += val * wp

print(abs(pos.real) + abs(pos.imag))
