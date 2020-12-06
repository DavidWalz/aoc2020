# https://adventofcode.com/2020/day/6
from collections import Counter

groups = open("6.txt").read().split("\n\n")

# number of people and individual answers per group
people = [len(g.split("\n")) for g in groups]
answers = [Counter(g.replace("\n", "")) for g in groups]


# part 1: number of answers given by anyone in the groups
n = [len(a) for a in answers]
print(sum(n))

# part 2: number of answers given by everyone in the groups
n = [sum([ai == p for ai in a.values()]) for a, p in zip(answers, people)]
print(sum(n))
