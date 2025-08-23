file = open('day8.txt', 'r')
lines = file.readlines()

x = 0
y = 0
antennas = {}
for li in range(len(lines)):
    x += 1
    y = len(lines[li].strip())

    vals = list(lines[li].strip())

    for vi in range(len(vals)):
        if vals[vi] != '.':
            if vals[vi] in antennas:
                antennas[vals[vi]].append((li, vi))
            else:
                antennas[vals[vi]] = [(li, vi)]


anti = set()
for antenna in antennas:
    locations = antennas[antenna]

    pairs = []
    for i in range(len(locations) - 1):
        for j in range(i + 1, len(locations)):
            pairs.append((locations[i], locations[j]))

    for p in pairs:
        p1 = p[0]
        p2 = p[1]

        anti.add(p1)
        anti.add(p2)

        xdiff = abs(p2[0] - p1[0])
        ydiff = abs(p2[1] - p1[1])

        p1_found = True
        p2_Found = True

        while p1_found or p2_Found:
            y1 = 0
            y2 = 0

            x1 = p1[0] - xdiff
            x2 = p2[0] + xdiff

            if p1[1] < p2[1]:
                y1 = p1[1] - ydiff
                y2 = p2[1] + ydiff
            elif p1[1] > p2[1]:
                y1 = p1[1] + ydiff
                y2 = p2[1] - ydiff    
            else:
                y1 = p1[1]
                y2 = p2[1] 

            if not (y1 < 0 or y1 >= y or x1 < 0 or x1 >= x):
                anti.add((x1, y1))
            else:
                p1_found = False

            if not (y2 < 0 or y2 >= y or x2 < 0 or x2 >= x):
                anti.add((x2, y2))
            else:
                p2_Found = False

            p1 = (x1,y1)
            p2 = (x2,y2)

print(len(anti))

    