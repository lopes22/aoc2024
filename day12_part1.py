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
        perim = 0
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
                perim += 1
            else:
                q.append((cur_r - 1, cur_c))

            # bottom
            if cur_r + 1 == max_r or grid[cur_r + 1][cur_c] != p:
                perim += 1
            else:
                q.append((cur_r + 1, cur_c))

            # left
            if cur_c - 1 < 0 or grid[cur_r][cur_c - 1] != p:
                perim += 1
            else:
                q.append((cur_r, cur_c - 1))

            # right
            if cur_c + 1 == max_c or grid[cur_r][cur_c + 1] != p:
                perim += 1
            else:
                q.append((cur_r, cur_c + 1))   

        seen.update(s)
        t += area * perim

print(t)