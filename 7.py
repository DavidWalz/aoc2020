# https://adventofcode.com/2020/day/7


# read and parse rules
lines = open("7.txt").read().split("\n")
D = {}
for l in lines:
    container, rule = l.split(" bags contain ")
    D[container] = {}
    if rule == "no other bags.":
        continue
    for c in rule.split(", "):
        r = c.split(" ")
        amount = r[0]
        color = " ".join(r[1:3])
        D[container][color] = int(amount)


# part 1
def possible_container(c: str):
    # recursively look for bags to contain a shiny gold bag
    for ci in D[c].keys():
        if ci == "shiny gold" or possible_container(ci):
            return True
    return False


print(sum([possible_container(c) for c in D.keys()]))


# part 2
def count_bags(c: str):
    return 1 + sum(ni * count_bags(ci) for ci, ni in D[c].items())


print(count_bags("shiny gold") - 1)  # don't count the shiny gold bag itself
