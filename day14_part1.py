
file = open('day14.txt', 'r')
lines = file.readlines()

bots = []
for line in lines:
    s = line.strip().split(' ')

    ps = s[0].split('=')[1].split(',')
    vs = s[1].split('=')[1].split(',')

    b = ((int(ps[0]), int(ps[1])), (int(vs[0]), int(vs[1])))

    bots.append(b)


w = 101
h = 103
ticks = 100

mw = w // 2
mh = h // 2

pos = [_[0] for _ in bots]

for t in range(ticks):
    for bi in range(len(bots)):
        cur_p = pos[bi]
        v = bots[bi][1]

        xv = v[0]
        xy = v[1]

        new_x = (cur_p[0] + xv) % w
        new_y = (cur_p[1] + xy) % h

        pos[bi] = (new_x, new_y)
                

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for p in pos:
    if p[0] == mw:
        continue
    if p[1] == mh:
        continue

    if p[0] < mw and p[1] < mh:
        q1 += 1
    elif p[0] > mw and p[1] < mh:
        q2 += 1
    elif p[0] < mw and p[1] > mh:
        q3 += 1
    else:
        q4 += 1

print(q1 * q2 * q3 * q4)
    