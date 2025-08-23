
file = open('day19.txt', 'r')
lines = file.readlines()

towels = set()

[towels.add(x) for x in lines[0].strip().split(', ')]

towel_count = {}

for t in towels:
    if t[0] in towel_count:
        towel_count[t[0]]  = max(towel_count[t[0]], len(t))
    else:
        towel_count[t[0]] = len(t)

patterns = []
for i in range(2, len(lines)):
    patterns.append(lines[i].strip())

def pattern_is_possible(pattern):
    if pattern == '':
        return True
    
    cur_s = pattern[0]

    if cur_s not in towel_count:
        return False
    
    c = min(towel_count[cur_s], len(pattern))

    for ci in range(c, 0, -1):
        p = pattern[:ci]

        if p in towels:
            result = pattern_is_possible(pattern[ci:])

            if result:
                return result

    return False

total = 0
for p in patterns:
    r = pattern_is_possible(p)

    if r:
        total += 1

print(total)
    
