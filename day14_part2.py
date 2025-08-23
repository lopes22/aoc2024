
file = open('day14.txt', 'r')
lines = file.readlines()

ff = open('test.txt', 'w')

bots = []
for line in lines:
    s = line.strip().split(' ')

    ps = s[0].split('=')[1].split(',')
    vs = s[1].split('=')[1].split(',')

    b = ((int(ps[0]), int(ps[1])), (int(vs[0]), int(vs[1])))

    bots.append(b)


w = 101
h = 103

mw = w // 2
mh = h // 2

pos = [_[0] for _ in bots]
seen = {}

c = 0
for pi in range(len(pos)):
    seen[pi] = set()
    seen[pi].add(pos[pi])

t = 0
while True:
    if c == len(bots):
         print(t)
         break
    
    t += 1
    
    for bi in range(len(bots)):
        cur_p = pos[bi]
        v = bots[bi][1]

        xv = v[0]
        xy = v[1]

        new_x = (cur_p[0] + xv) % w
        new_y = (cur_p[1] + xy) % h

        pos[bi] = (new_x, new_y)

        if pos[bi] in seen[bi]:
                c += 1


    for hh in range(h):
        ss = ''
        for ww in range(w):
            if (ww, hh) in pos:
                ss += 'B'
            else:
                ss += '.'
        ff.write(ss + '\n')
    
    ff.write('***' + str(t) + '***' + '\n')

    