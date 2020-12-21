# https://adventofcode.com/2020/day/21

allergens = {}
all_ingredients = []

for line in open("21.txt").read().split("\n"):
    ingr, allg = line.rstrip(")").split(" (contains ")
    ingr = ingr.split(" ")
    all_ingredients += ingr
    for a in allg.split(", "):
        if a in allergens:
            allergens[a] = allergens[a].intersection(ingr)
        else:
            allergens[a] = set(ingr)

while True:
    uniques = [list(s)[0] for s in allergens.values() if len(s) == 1]
    if len(uniques) == len(allergens):
        break
    for unique in uniques:
        for ingredients in allergens.values():
            if unique in ingredients and len(ingredients) != 1:
                ingredients.remove(unique)

# part 1
safe = set(all_ingredients) ^ set.union(*allergens.values())
print(sum([all_ingredients.count(ingr) for ingr in safe]))

# part 2
print(','.join([list(allergens[a])[0] for a in sorted(allergens)]))
