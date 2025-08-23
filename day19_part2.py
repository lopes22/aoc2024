
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

good_p = {}
bad_p = set()

def pattern_is_possible(pattern):
    if pattern == '':
        return 1
    
    if pattern in good_p:
        return good_p[pattern]
    
    cur_s = pattern[0]

    if cur_s not in towel_count:
        return 0
    
    c = min(towel_count[cur_s], len(pattern))

    tt = 0
    for ci in range(c, 0, -1):
        p = pattern[:ci]
        if p in towels:
            tt += pattern_is_possible(pattern[ci:])

    good_p[pattern] = tt
    return tt

total = 0
for p in patterns:
    total += pattern_is_possible(p)

print(total)
    
