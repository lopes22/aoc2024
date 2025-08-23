import sys

file = open('day10.txt', 'r')
lines = file.readlines()

trail_heads = []
grid = []
r = 0
for line in lines:
    pos = [int(x) for x in line.strip()]
    c = 0
    for p in pos:
        if p == 0:
            trail_heads.append((r,c))
        c += 1
    
    grid.append(pos)
    r+= 1

row_c = len(grid)
col_c = len(grid[0])

thc = 0
for th in trail_heads:
    q = []
    seen = set()
    q.append((th, 0, seen))
    while len(q) > 0:
        cur = q.pop(0)

        pos = cur[0]
        row = pos[0]
        col = pos[1]
        p = cur[1]
        s = cur[2]

        if p == 9:
            thc += 1
            continue

        ss = s.copy()
        ss.add(pos)

        #top
        if row - 1 >= 0 and (row - 1, col) not in s and grid[row - 1][col] == p + 1:   
            q.append(((row - 1, col), p + 1, ss))

        #bottom
        if row + 1 < row_c and (row + 1, col) not in s and grid[row + 1][col] == p + 1:
            q.append(((row + 1, col), p + 1, ss))

        #right
        if col + 1 < col_c and (row, col + 1) not in s and grid[row][col + 1] == p + 1:  
            q.append(((row, col + 1), p + 1, ss))

        #left
        if col - 1 >= 0 and (row, col - 1) not in s and grid[row][col - 1] == p + 1:   
            q.append(((row, col - 1), p + 1, ss))

print(thc)






    