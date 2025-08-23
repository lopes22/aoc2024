
file = open('day2.txt', 'r')
lines = file.readlines()

safe = 0

rows = []

for line in lines:
    line = line.strip()
    split = line.split(' ')

    levels = [int(x) for x in split]
    rows.append(levels)

for row in rows:
    incr = False
    decr = False
    if row[0] == row[1]:
        continue
    
    if row[0] > row[1]:
        decr = True
    else:
        incr = True

    if abs(row[0] - row[1]) > 3:
        continue

    valid = True
    for i in range(1, len(row) - 1):
        if incr:
            if row[i] >= row[i + 1]:
                valid = False
                break
        else:
            if row[i] <= row[i + 1]:
                valid = False
                break
        
        if abs(row[i] - row[i + 1]) > 3:
            valid = False
            break
    
    if valid:
        safe += 1

print(safe)