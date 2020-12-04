# https://adventofcode.com/2020/day/4
import re


passports = [
    {k: v for k, v in [e.split(":") for e in passport.split()]}
    for passport in open("4.txt").read().split("\n\n")
]

required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def check(p, part2=False):
    if not required.issubset(p.keys()):
        return False
    if not part2:
        return True

    valid = True

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    valid &= 1920 <= int(p["byr"]) <= 2002

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    valid &= 2010 <= int(p["iyr"]) <= 2020

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    valid &= 2020 <= int(p["eyr"]) <= 2030

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if p["hgt"].endswith("cm"):
        valid &= 150 <= int(p["hgt"].strip("cm")) <= 193
    else:
        valid &= 59 <= int(p["hgt"].strip("in")) <= 76

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    valid &= re.match(r"^#(?:[0-9a-fA-F]{6})$", p["hcl"]) is not None

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    valid &= p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    valid &= re.match(r"^(?:[0-9]{9})$", p["pid"]) is not None

    return valid


# part 1
print(sum([check(p) for p in passports]))

# part 2
print(sum([check(p, True) for p in passports]))
