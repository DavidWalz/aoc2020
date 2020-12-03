# https://adventofcode.com/2020/day/2
lines = open("2.txt").read().split("\n")


def parse(line):
    policy, password = line.split(": ")
    numbers, char = policy.split(" ")
    n1, n2 = numbers.split("-")
    return int(n1), int(n2), char, password


# part 1
n_valid = 0
for n1, n2, char, pw in map(parse, lines):
    n_valid += n1 <= pw.count(char) <= n2
print(n_valid)

# part 2
n_valid = 0
for n1, n2, char, pw in map(parse, lines):
    n_valid += (pw[n1 - 1] == char) != (pw[n2 - 1] == char)  # xor
print(n_valid)
