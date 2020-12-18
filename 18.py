# https://adventofcode.com/2020/day/18

# Solution from https://github.com/erijpkema/advent_of_code_2020/blob/main/day18.py
# based on a recipe from https://code.activestate.com/recipes/384122/
# Nothing to add.
class Infix(object):
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)


mul = Infix(lambda x, y: x * y)
add = Infix(lambda x, y: x + y)

lines = open('18.txt').readlines()

# part 1
def process1(line, part=1):
    line = line.replace('*', '|mul|').replace('+', '|add|')
    return eval(line)

print(sum(map(process1, lines)))

# part 2
def process2(line, part=1):
    line = line.replace('*', '|mul|')
    return eval(line)

print(sum(map(process2, lines)))
