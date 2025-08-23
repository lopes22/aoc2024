import re

file = open('day3.txt', 'r')
lines = file.readlines()
a = ""

for l in lines:
    a += l

total = 0
groups = re.findall('(mul\(\d+,\d+\))', a)

for g in groups:
    nums = re.findall('(\d+)', g)
    total += int(nums[0]) * int(nums[1])

print(total)