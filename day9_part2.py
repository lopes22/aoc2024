import sys

file = open('day9.txt', 'r')
lines = file.readlines()

l = lines[0].strip()

free = {}
i = 0
cur_i = 0
t = 0
locations = {}
iid = -1
while i < len(l):
    if i % 2 != 0:
        f = int(l[i])

        if f > 0:
            if f in free:
                free[f].append(cur_i)
                free[f].sort()
            else:
                free[f] = [cur_i]

        cur_i += f

    else:
        iid += 1
        locations[iid] = (cur_i, int(l[i]))
        cur_i += int(l[i])

    i += 1

for id in range(iid, 0, -1):
    myloc = locations[id]
    v = myloc[1]

    k = list(free.keys())
    k.sort()

    sel_f = None
    sel_k = None
    min_i = sys.maxsize
    for ke in k:
        if ke < v:
            continue
        if ke >= v:
            pf = free[ke]

            if pf[0] < myloc[0] and pf[0] < min_i:
                sel_k = ke
                min_i = pf[0]

    if sel_k != None:
        sel_f = free[sel_k].pop(0)
    else:
        continue

    if len(free[sel_k]) == 0:
        del free[sel_k]

    if sel_f != None:
        c = sel_f + int(v)

        locations[id] = (sel_f, v)

        result = sel_k - v
        if result > 0:
            if result in free:
                free[result].append(c)
                free[result].sort()
            else:
                free[result] = [c]

for loc in locations.keys():
    abc = locations[loc]
    curcur = abc[0]
    for j in range(abc[1]):
        t += loc * curcur
        curcur += 1

print(t)






    