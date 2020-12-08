# https://adventofcode.com/2020/day/8
import numpy as np

cmds = np.array([cmd.split() for cmd in open("8.txt").read().split("\n")])


def execute(cmds):
    visited = np.zeros(len(cmds), int)
    acc = 0
    pos = 0
    while pos < len(cmds):
        if visited[pos]:
            break
        c, v = cmds[pos]
        visited[pos] += 1
        if c == "acc":
            acc += int(v)
            pos += 1
        elif c == "jmp":
            pos += int(v)
        else:  # nop
            pos += 1
    terminated = pos == len(cmds)
    return terminated, acc


# part 1
print(execute(cmds))

# part 2
for i, (c, v) in enumerate(cmds):
    if c == "acc":
        continue
    new_cmds = cmds.copy()
    new_cmds[i][0] = "nop" if c == "jmp" else "jmp"
    r, acc = execute(new_cmds)
    if r:
        print(acc)
        break
