file = open('day4.txt', 'r')
lines = file.readlines()

grid = []
for l in lines:
    grid.append(list(l.strip()))

c = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] != 'A':
            continue

        #bottom right top left
        if y + 1 < len(grid[x]) and x + 1 < len(grid) and y - 1 >= 0 and x - 1 >= 0:
            if not ((grid[x + 1][y + 1] == 'M' and grid[x - 1][y - 1] == 'S') or (grid[x + 1][y + 1] == 'S' and grid[x - 1][y - 1] =='M')):
                continue
        else:
            continue
        #bottom left top right
        if y - 1 >= 0 and x + 1 < len(grid) and y + 1 < len(grid[x]) and x - 1 >= 0:
            if not ((grid[x + 1][y - 1] == 'M' and grid[x - 1][y + 1] == 'S') or (grid[x + 1][y - 1] == 'S' and grid[x - 1][y + 1] == 'M')):
                continue
        else:
            continue
        
        c += 1
            
print(c)