# https://adventofcode.com/2020/day/14g

cmds = [line.split(" = ") for line in open("14.txt").read().split("\n")]


# part 1: memory value decoder
memory = {}


def apply_mask(c_val, c_mask):
    return {"0": "0", "1": "1"}.get(c_mask, c_val)


for cmd, val in cmds:
    if cmd == "mask":
        mask = val
    else:
        addr = int(cmd.strip("me[]"))
        val = f"{int(val):036b}"
        val = "".join(map(apply_mask, val, mask))
        memory[addr] = int(val, 2)

print(sum(memory.values()))


# part 2: memory address decoder
# template logic from https://github.com/codertee/adventofcode/blob/main/adventofcode/solutions/y2020/d14_binary.py
memory = {}


def apply_mask(c_val, c_mask):
    return {"1": "1", "X": "{}"}.get(c_mask, c_val)


for cmd, val in cmds:
    if cmd == "mask":
        mask = val
        n_float = mask.count("X")
    else:
        addr = int(cmd.strip("me[]"))
        addr = f"{addr:036b}"
        template = "".join(map(apply_mask, addr, mask))
        for f in range(2 ** n_float):
            addr = template.format(*f"{f:0{n_float}b}")
            memory[int(addr, 2)] = int(val)

print(sum(memory.values()))