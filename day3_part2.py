import re

file = open('day3.txt', 'r')
lines = file.readlines()
a = ""

for l in lines:
    a += l

total = 0
disabled = False
groups = re.findall('(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', a)

for g in groups:
    if g == "don't()":
        disabled = True
    elif g == "do()":
        disabled = False
    else:
        if disabled:
            continue

        nums = re.findall('(\d+)', g)
        total += int(nums[0]) * int(nums[1])

print(total)