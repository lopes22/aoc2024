
file = open('day18.txt', 'r')
lines = file.readlines()

mem = set()

c = 0
for l in lines:
    if c == 1024:
        break
    line = l.strip().split(',')
    mem.add((int(line[0]), int(line[1])))

    c += 1

q = [((0,0), 0)]
seen = set()

while len(q) > 0:
    cur = q.pop(0)
    coord = cur[0]
    steps = cur[1]

    if coord in seen or coord in mem:
        continue

    seen.add(coord)

    if coord == (70,70):
         print(steps)
         break

    r = coord[0]
    c = coord[1]

    if r - 1 >= 0:
        q.append(((r - 1, c), steps + 1))

    if r + 1 <= 70:
        q.append(((r + 1, c), steps + 1))

    if c - 1 >= 0:
        q.append(((r, c - 1), steps + 1))

    if c + 1 <= 70:
        q.append(((r, c + 1), steps + 1))