import sys
import copy

file = open('day16.txt', 'r')
lines = file.readlines()

start = None
end = None
walls = set()

for x in range(0, len(lines)):
    for y in range(0, len(lines[x].strip())):
        if lines[x][y] == '#':
            walls.add((x, y))
        elif lines[x][y] == 'S':
            start = (x, y)
        elif lines[x][y] == 'E':
            end = (x, y)

def possible_moves(cur, d):
    north = (cur[0] - 1, cur[1])
    south = (cur[0] + 1, cur[1])
    east = (cur[0], cur[1] + 1)
    west = (cur[0], cur[1] - 1)

    if (d == 'E'):
        return [('E', east), ('N', north), ('S', south)]
    
    if (d == 'N'):
        return [('E', east), ('N', north), ('W', west)]
    
    if (d == 'S'):
        return [('E', east), ('S', south), ('W', west)]
    
    if (d == 'W'):
        return [('W', west), ('S', south), ('N', north)]

score = sys.maxsize
begin_set = []
begin_set.append(start)
s = [(start, 'E', 0, begin_set)]
seen = {}
scores = []
while s:
    cur = s.pop(0)

    p = cur[0]
    d = cur[1]
    scr = cur[2]
    path = cur[3]

    if p == end:
        score = min(score, scr)
        scores.append((scr, path))
        continue

    if (p,d) in seen and seen[(p,d)] < scr:
        continue

    seen[(p,d)] = scr
    
    moves = possible_moves(p, d)

    for m in moves:
        if m[1] in walls:
            continue

        if m[0] == d:
            n_p = copy.deepcopy(path)
            n_p.append(m[1])
            s.append((m[1], m[0], scr + 1, n_p))
        else:
            n_p = copy.deepcopy(path)
            n_p.append(m[1])
            s.append((m[1], m[0], scr + 1001, n_p))

final = set()

for sc in scores:
    if sc[0] != score:
        continue
    final = final.union(sc[1])

print(len(final))