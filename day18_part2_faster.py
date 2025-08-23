
file = open('day18.txt', 'r')
lines = file.readlines()


memory = []

for l in lines:
    line = l.strip().split(',')
    memory.append((int(line[0]), int(line[1])))

start = 1025
end = len(memory) - 1

cur_min = len(memory) - 1
while start <= end:

    i = start + ((end - start) // 2)

    q = [((0,0), 0)]
    seen = set()
    mem = set(memory[0:i])

    found = False
    while len(q) > 0:
        cur = q.pop(0)
        coord = cur[0]
        steps = cur[1]

        if coord in seen or coord in mem:
            continue

        seen.add(coord)

        if coord == (70,70):
            found = True
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

    if not found:
        end = i - 1
        cur_min = i
    else:
        start = i + 1

print(memory[cur_min - 1])
