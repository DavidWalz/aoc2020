# https://adventofcode.com/2020/day/14g
import numpy as np

lines = open("14.txt").read().split("\n")


# part 1: memory value decoder
memory = {}
pows = 2 ** np.arange(36, dtype=np.int64)[::-1]


for line in lines:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
        mask_idx = [i for i, v in enumerate(mask) if v != "X"]
        mask_val = [int(v) for i, v in enumerate(mask) if v != "X"]
        continue

    addr, val = line.split(" = ")
    addr = int(addr.strip("me[]"))
    val = int(val)
    b = np.fromiter([i for i in f"{val:036b}"], dtype=int)
    b[mask_idx] = mask_val
    memory[addr] = np.dot(b, pows)

print(sum(memory.values()))


# part 2: memory address decoder
# implementation of floating logic from https://github.com/codertee/adventofcode/blob/main/adventofcode/solutions/y2020/d14_binary.py
memory = {}

for line in lines:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
        continue

    addr, val = line.split(" = ")
    addr = int(addr.strip("me[]"))
    val = int(val)

    addr = f"{addr:036b}"
    addr_template = ""
    for mask_bit, addr_bit in zip(mask, addr):
        if mask_bit == "0":
            addr_template += addr_bit
        elif mask_bit == "1":
            addr_template += "1"
        else:
            addr_template += "{}"

    floating_length = mask.count('X')
    for f in range(2 ** floating_length):
        addr = addr_template.format(*f"{f:0{floating_length}b}")
        addr = int(addr, 2)
        memory[addr] = val

print(sum(memory.values()))