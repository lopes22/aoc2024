import sys

file = open('day12.txt', 'r')
lines = file.readlines()

grid = []

for r in range(len(lines)):
    grid.append(list(lines[r].strip()))

max_r = len(grid)
max_c = len(grid[0])

seen = set()
t = 0
for row in range(max_r):
    for col in range(max_c):

        coord = (row, col)
        if coord in seen:
            continue

        seen.add(coord)

        area = 0
        perims = []
        p = grid[row][col]

        q = [coord]
        s = set()

        while len(q) > 0:
            cur = q.pop(0)

            cur_r = cur[0]
            cur_c = cur[1]

            if (cur_r, cur_c) in s:
                continue

            s.add((cur_r, cur_c))
            area += 1

            #top
            if cur_r - 1 < 0 or grid[cur_r - 1][cur_c] != p:
                perims.append((cur, 'T'))
            else:
                q.append((cur_r - 1, cur_c))

            # bottom
            if cur_r + 1 == max_r or grid[cur_r + 1][cur_c] != p:
                perims.append((cur, 'B'))
            else:
                q.append((cur_r + 1, cur_c))

            # left
            if cur_c - 1 < 0 or grid[cur_r][cur_c - 1] != p:
                perims.append((cur, 'L'))
            else:
                q.append((cur_r, cur_c - 1))

            # right
            if cur_c + 1 == max_c or grid[cur_r][cur_c + 1] != p:
                perims.append((cur, 'R'))
            else:
                q.append((cur_r, cur_c + 1))   

        seen.update(s)

        p_seen = set()
        side_c = 0

        for fp in perims:
            if fp in p_seen:
                continue

            side_c += 1

            p_seen.add(fp)

            if fp[1] == 'T':
                c = (fp[0][0], fp[0][1] - 1)
                while (c, 'T') in perims:
                    p_seen.add((c, 'T'))
                    c = (c[0], c[1] - 1)

                c = (fp[0][0], fp[0][1] + 1)
                while (c, 'T') in perims:
                    p_seen.add((c, 'T'))
                    c = (c[0], c[1] + 1)

            if fp[1] == 'B':
                c = (fp[0][0], fp[0][1] - 1)
                while (c, 'B') in perims:
                    p_seen.add((c, 'B'))
                    c = (c[0], c[1] - 1)


                c = (fp[0][0], fp[0][1] + 1)
                while (c, 'B') in perims:
                    p_seen.add((c, 'B'))
                    c = (c[0], c[1] + 1)

            if fp[1] == 'L':
                c = (fp[0][0] - 1, fp[0][1])
                while (c, 'L') in perims:
                    p_seen.add((c, 'L'))
                    c = (c[0] - 1, c[1])

                c = (fp[0][0] + 1, fp[0][1])
                while (c, 'L') in perims:
                    p_seen.add((c, 'L'))
                    c = (c[0] + 1, c[1])

            if fp[1] == 'R':
                c = (fp[0][0] - 1, fp[0][1])
                while (c, 'R') in perims:
                    p_seen.add((c, 'R'))
                    c = (c[0] - 1, c[1])

                c = (fp[0][0] + 1, fp[0][1])
                while (c, 'R') in perims:
                    p_seen.add((c, 'R'))
                    c = (c[0] + 1, c[1])

        t += area * side_c

print(t)