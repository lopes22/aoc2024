file = open('day4.txt', 'r')
lines = file.readlines()

grid = []
for l in lines:
    grid.append(list(l.strip()))

c = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        #right
        if y + 3 < len(grid[x]):
            if grid[x][y] == 'X' and grid[x][y + 1] == 'M' and grid[x][y + 2] == 'A' and grid[x][y + 3] == 'S':
                c += 1
        #left
        if y - 3 >= 0:
            if grid[x][y] == 'X' and grid[x][y - 1] == 'M' and grid[x][y - 2] =='A' and grid[x][y - 3] == 'S':
                c += 1
        #top
        if x - 3 >= 0:
            if grid[x][y] == 'X' and grid[x - 1][y] == 'M' and grid[x - 2][y] =='A' and grid[x - 3][y] == 'S':
                c += 1
        #bottom
        if x + 3 < len(grid):
            if grid[x][y] == 'X' and grid[x + 1][y] == 'M' and grid[x + 2][y] =='A' and grid[x + 3][y] == 'S':
                c += 1
        #bottom right
        if y + 3 < len(grid[x]) and x + 3 < len(grid):
            if grid[x][y] == 'X' and grid[x + 1][y + 1] == 'M' and grid[x + 2][y + 2] =='A' and grid[x + 3][y + 3] == 'S':
                c += 1
        #bottom left
        if y - 3 >= 0 and x + 3 < len(grid):
            if grid[x][y] == 'X' and grid[x + 1][y - 1] == 'M' and grid[x + 2][y - 2] =='A' and grid[x + 3][y - 3] == 'S':
                c += 1
        #top left
        if y - 3 >= 0 and x - 3 >= 0:
            if grid[x][y] == 'X' and grid[x - 1][y - 1] == 'M' and grid[x - 2][y - 2] =='A' and grid[x - 3][y - 3] == 'S':
                c += 1
        #top right
        if y + 3 < len(grid[x]) and x - 3 >= 0:
            if grid[x][y] == 'X' and grid[x - 1][y + 1] == 'M' and grid[x - 2][y + 2] =='A' and grid[x - 3][y + 3] == 'S':
                c += 1
            
print(c)