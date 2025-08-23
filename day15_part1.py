
file = open('day15.txt', 'r')
lines = file.readlines()

moves = ''
walls = set()
boxes = set()
i = 0
r = 0
start = None
while lines[i] != '\n':
    l = lines[i].strip()

    for s in range(len(l)):
        if l[s] == '@':
            start = (r, s)
        
        if l[s] == '#':
            walls.add((r, s))

        if l[s] == 'O':
            boxes.add((r, s))

    i += 1
    r += 1

i += 1

while i < len(lines):
    moves += lines[i].strip()

    i += 1

cur = start

for m in moves:
    n = None
    if m == '^':
        n = (cur[0] - 1, cur[1])
    elif m == 'v':
        n = (cur[0] + 1, cur[1])
    elif m == '<':
        n = (cur[0], cur[1] - 1)
    else:
        n = (cur[0], cur[1] + 1)

    if n in walls:
        continue
    elif n in boxes:
        fw = False
        b = n
        while b in boxes:
            n_b = None
            if m == '^':
                n_b = (b[0] - 1, b[1])
            elif m == 'v':
                n_b = (b[0] + 1, b[1])
            elif m == '<':
                n_b = (b[0], b[1] - 1)
            else:
                n_b = (b[0], b[1] + 1)

            if n_b in walls:
                fw = True
                break

            b = n_b

        if fw:
            continue
        else:
            cur = n

            boxes.remove(n)
            boxes.add(b)
    else:
        cur = n

t = 0

for fb in boxes:
    t += (100 * fb[0]) + fb[1]

print(t)