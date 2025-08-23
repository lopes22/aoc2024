file = open('day5.txt', 'r')
lines = file.readlines()

rules = {}
i = 0
while True:
    if lines[i].strip() == '':
        i += 1
        break
    
    s = lines[i].strip().split('|')

    if s[0] in rules:
        rules[s[0]].add(s[1])
    else:
        rules[s[0]] = {s[1]}
    i += 1

updates = [];    
while i < len(lines):
    updates.append(lines[i].strip().split(','))
    i += 1
     
total = 0
for u in updates:
    invalid = False
    for pi in range(1, len(u)):
        if invalid:
            break

        if u[pi] not in rules:
            continue

        r = rules[u[pi]]

        for p in range(pi):
            if u[p] in r:
                invalid = True
                break
    
    if invalid:
        for pi in range(1, len(u)):

            if u[pi] not in rules:
                continue

            r = rules[u[pi]]

            p = pi - 1
            c = pi
            while p >= 0:
                if u[p] in r:
                    t = u[p]
                    u[p] = u[c]
                    u[c] = t
                    c = p

                p -= 1

        middle = len(u) // 2
        total += int(u[middle])

print(total)