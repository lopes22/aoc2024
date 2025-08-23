file = open('day6.txt', 'r')
lines = file.readlines()

grid = []
start = None
cur_x_dir = -1
cur_y_dir = 0
cur_d = 0
d = [-1, 1, 1, -1]
for i in range(len(lines)):
    r = list(lines[i].strip())

    if '^' in r:
        start = (i, r.index('^'))

    grid.append(r)

cur = (start[0], start[1])
max_x = len(grid)
max_y = len(grid[0])
seen = set()
while True:
    seen.add(cur)

    next_x = cur[0] + cur_x_dir
    next_y = cur[1] + cur_y_dir
    if next_x < 0 or next_x == max_x or next_y < 0 or next_y == max_y:
        break
    
    if grid[next_x][next_y] == '#':
        cur_d += 1
        change = d[cur_d % 4]
        cur_x_dir = ((cur_x_dir + change) % 2) * change
        cur_y_dir = ((cur_y_dir + change) % 2) * change
    else:
        cur = (next_x, next_y)

seen.remove(start)

c = 0
for s in seen:
    states = set()
    grid[s[0]][s[1]] = '#'

    cur_x_dir = -1
    cur_y_dir = 0
    cur_d = 0
    cur = (start[0], start[1], cur_x_dir, cur_y_dir)
    while True:
        
        if cur in states:
            c += 1
            break
        else:
            states.add(cur)

        next_x = cur[0] + cur_x_dir
        next_y = cur[1] + cur_y_dir
        if next_x < 0 or next_x == max_x or next_y < 0 or next_y == max_y:
            break
        
        if grid[next_x][next_y] == '#':
            cur_d += 1
            change = d[cur_d % 4]
            cur_x_dir = ((cur_x_dir + change) % 2) * change
            cur_y_dir = ((cur_y_dir + change) % 2) * change

            cur = (cur[0], cur[1], cur_x_dir, cur_y_dir)
        else:
            cur = (next_x, next_y, cur_x_dir, cur_y_dir)

    grid[s[0]][s[1]] = '.'

print(c)