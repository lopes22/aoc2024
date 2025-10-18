
file = open('day20.txt', 'r')
lines = file.readlines()

start = None
end = None

walls = set()

saved = 100

max_r = len(lines) - 3
max_c = len(lines[0].strip()) - 3

for row in range(1, len(lines) - 1):
    l = lines[row].strip()
    for col in range(1, len(l) - 1):
        if l[col] == '#':
            walls.add((row - 1, col - 1))
        elif l[col] == 'S':
            start = (row - 1, col - 1)
        elif l[col] == 'E':
            end = (row - 1, col - 1)

q = []
seen = set()

q.append((start, [start]))

s_p = []

while len(q) > 0:
    cur = q.pop(0)

    loc = cur[0]
    if loc == end:
        s_p = cur[1]
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


d = {}
counter = 0
for x in s_p:
    d[x] = counter
    counter += 1
    
cheats_c = 0
sps = set(s_p)


for sp_l in s_p[:-1]:
    r = sp_l[0]
    c = sp_l[1]

    up = (r - 1, c)
    up2 = (r - 2, c)
    down = (r + 1, c)
    down2 = (r + 2, c)
    right = (r, c + 1)
    right2 = (r, c + 2)
    left = (r, c - 1)
    left2 = (r, c - 2)

    dd = d[sp_l]

    if up[0] >= 0 and up in walls and up2[0] >= 0 and up2 in sps:
        ddd = d[up2]
        if (ddd - dd - 2) >= saved:
            cheats_c += 1

    if down[0] <= max_r and down in walls and down2[0] <= max_r and down2 in sps:
        ddd = d[down2]
        if (ddd - dd - 2) >= saved:
            cheats_c += 1           

    if right[1] <= max_c and right in walls and right2[1] <= max_c and right2 in sps:
        ddd = d[right2]
        if (ddd - dd - 2) >= saved:
            cheats_c += 1     

    if left[1] >= 0 and left in walls and left2[1] >= 0 and left2 in sps:
        ddd = d[left2]
        if (ddd - dd - 2) >= saved:
            cheats_c += 1         

print(cheats_c)
