# https://adventofcode.com/2020/day/12

lines = open("12.txt").read().split("\n")


# part 1
heading = 90
compass = {"N": 0, "E": 90, "S": 180, "W": 270}
travelled = {0: 0, 90: 0, 180: 0, 270: 0}

for line in lines:
    h = line[0]
    d = int(line[1:])
    if h in ("L", "R"):  # turn
        sign = +1 if h == "R" else -1
        heading = (heading + sign * d) % 360
    elif h == "F":  # move along current heading
        travelled[heading] += d
    else:  # move in stated direction
        travelled[compass[h]] += d

print(abs(travelled[0] - travelled[180]) + abs(travelled[90] - travelled[270]))


# part 2
pe, pn = 0, 0  # ship position in easting / northing
we, wn = 10, 1  # waypoint, relative position in easting / northing

for line in lines:
    h = line[0]
    d = int(line[1:])

    # move waypoint
    if h == "N":
        wn += d
    if h == "S":
        wn -= d
    if h == "E":
        we += d
    if h == "W":
        we -= d

    # rotate waypoint
    if h in ("L", "R"):
        sign = +1 if h == "R" else -1
        if d == 90:
            we, wn = wn * sign, -we * sign
        if d == 180:
            we, wn = -we, -wn
        if d == 270:
            we, wn = -wn * sign, we * sign

    # move towards waypoint
    if h == "F":
        pe += d * we
        pn += d * wn

print(abs(pe) + abs(pn))