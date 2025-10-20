
file = open('day20.txt', 'r')
lines = file.readlines()

start = None
end = None

walls = set()

saved = 100

max_r = len(lines) - 1
max_c = len(lines[0].strip()) - 1

for row in range(len(lines)):
    l = lines[row].strip()
    for col in range(len(l)):
        if l[col] == '#':
            walls.add((row, col))
        elif l[col] == 'S':
            start = (row, col)
        elif l[col] == 'E':
            end = (row, col)

def find_sp():
    q = []
    seen = set()

    q.append((start, [start]))

    s_pp = []

    while len(q) > 0:
        cur = q.pop(0)

        loc = cur[0]
        if loc == end:
            s_pp = cur[1]
            break

        seen.add(loc)

        r = loc[0]
        c = loc[1]

        cur_path = cur[1]

        if r - 1 >= 0 and (r - 1, c) not in walls and (r - 1, c) not in seen:
            q.append(((r - 1, c), cur_path + [(r - 1, c)]))

        if r + 1 <= max_r and (r + 1, c) not in walls and (r + 1, c) not in seen:
            q.append(((r + 1, c), cur_path + [(r + 1, c)]))

        if c - 1 >= 0 and (r, c - 1) not in walls and (r, c - 1) not in seen: 
            q.append(((r, c - 1), cur_path + [(r, c - 1) ]))

        if c + 1 <= max_c and (r, c + 1) not in walls and (r, c + 1) not in seen:
            q.append(((r, c + 1), cur_path + [(r, c + 1)]))

    return s_pp


s_p = find_sp()


d = {}
counter = 0
for x in s_p:
    d[x] = counter
    counter += 1
    
cheats_c = 0

for sp_l in s_p[:-(saved + 2)]:
    dd = d[sp_l]

    available = s_p[dd + saved + 2:]

    rspl = sp_l[0]
    cspl = sp_l[1]

    for i in available:
        ri = i[0]
        ci = i[1]
        
        distance = abs(ri - rspl) + abs(ci - cspl)

        if distance <= 20 and (d[i] - dd - distance) >= saved:
            cheats_c += 1

print(cheats_c)
