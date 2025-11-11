
file = open('day21.txt', 'r')
lines = file.readlines()

codes = []

for l in lines:
    codes.append(l.strip())

keypad = [['7', '8' ,'9'], ['4', '5', '6'], ['1', '2', '3'], ['X', '0', 'A']]

directional = [['X', '^', 'A'], ['<', 'v', '>']]

keypad_map = {}
directional_map = {}

flat_keypad = [
    x
    for xs in keypad
    for x in xs
]

flat_directional = [
    x
    for xs in directional
    for x in xs
]

for kx in range(len(keypad)):
    for ky in range(len(keypad[0])):

        for e in flat_keypad:
            q = []

            q.append(((kx, ky), [], [(kx, ky)]))

            s = keypad[kx][ky]

            if s == 'X' or e == 'X':
                continue

            if s == e:
                keypad_map[(s, e)] = [[]]        
                continue        

            all_paths = []
            min_path = 100
            while len(q) > 0:
                c = q.pop(0)

                loc = c[0]
                locx = loc[0]
                locy = loc[1]
                p = c[1]
                seen = c[2]

                if keypad[locx][locy] == e:
                    min_path = min(min_path, len(p))
                    all_paths.append(p)
                    continue

                if locx + 1 < 4 and keypad[locx + 1][locy] != 'X' and (locx + 1, locy) not in seen:
                    q.append(((locx + 1, locy), p + ['v'], seen + [(locx + 1, locy)]))

                if locx - 1 >= 0 and keypad[locx - 1][locy] != 'X' and (locx - 1, locy) not in seen:
                    q.append(((locx - 1, locy), p + ['^'], seen + [(locx - 1, locy)]))

                if locy + 1 < 3 and keypad[locx][locy + 1] != 'X' and (locx, locy + 1) not in seen:
                    q.append(((locx, locy+ 1), p + ['>'], seen + [(locx, locy + 1)]))

                if locy - 1 >= 0 and keypad[locx][locy - 1] != 'X' and (locx, locy - 1) not in seen:
                    q.append(((locx, locy - 1), p + ['<'], seen + [(locx, locy - 1)]))

            
            # get the path with the least transistions
            results = [sublist for sublist in all_paths if len(sublist) == min_path]
            keypad_map[(s, e)] = results



for kx in range(len(directional)):
    for ky in range(len(directional[0])):

        for e in flat_directional:
            q = []

            q.append(((kx, ky), [], [(kx, ky)]))

            s = directional[kx][ky]

            if s == 'X' or e == 'X':
                continue

            if s == e:
                directional_map[(s, e)] = [[]]        
                continue                 

            all_paths = []
            min_path = 100
            while len(q) > 0:
                c = q.pop(0)

                loc = c[0]
                locx = loc[0]
                locy = loc[1]
                p = c[1]
                seen = c[2]

                if directional[locx][locy] == e:
                    min_path = min(min_path, len(p))
                    all_paths.append(p)
                    continue

                if locx + 1 < 2 and directional[locx + 1][locy] != 'X' and (locx + 1, locy) not in seen:
                    q.append(((locx + 1, locy), p + ['v'], seen + [(locx + 1, locy)]))

                if locx - 1 >= 0 and directional[locx - 1][locy] != 'X' and (locx - 1, locy) not in seen:
                    q.append(((locx - 1, locy), p + ['^'], seen + [(locx - 1, locy)]))

                if locy + 1 < 3 and directional[locx][locy + 1] != 'X' and (locx, locy + 1) not in seen:
                    q.append(((locx, locy + 1), p + ['>'], seen + [(locx, locy + 1)]))

                if locy - 1 >= 0 and directional[locx][locy - 1] != 'X' and (locx, locy - 1) not in seen:
                    q.append(((locx, locy - 1), p + ['<'], seen + [(locx, locy - 1)]))

            # get the path with the least transistions
            results = [sublist for sublist in all_paths if len(sublist) == min_path]
            directional_map[(s, e)] = results

def find_keypad_path(goal, start):
    paths = keypad_map[goal]

    if len(paths) == 1:
        return paths[0]
    
    tpaths = []
    for rpath in paths:
        tcount = 0
        startt = start
        for path_item in rpath:
            if startt != path_item:
                tcount += 1
                startt = path_item
        tpaths.append((tcount, rpath))

    tpaths.sort()
    return tpaths[0][0]

def find_directional_path(goal, start):
    paths = directional_map[goal]

    if len(paths) == 1:
        return paths[0]
    
    tpaths = []
    for rpath in paths:
        tcount = 0
        startt = start
        for path_item in rpath:
            if startt != path_item:
                tcount += 1
                startt = path_item
        tpaths.append((tcount, rpath))

    tpaths.sort()
    return tpaths[0][1]      


# total = 0                        
# for code in codes:
#     commands = []
#     robots = ['A', 'A', 'A']  #robot pointers     

#     for i1 in code:
#         start1 = robots[0]
#         p1 = find_keypad_path((start1, i1), robots[0]) + ['A'] # commands for robot 1
#         for i2 in p1:
#             start2 = robots[1]
#             p2 = find_directional_path((start2, i2), robots[2]) + ['A'] # commands for robot 2
#             for i3 in p2:
#                 start3 = robots[2]
#                 p3 = find_directional_path((start3, i3), 'A') + ['A'] # commands for robot 3
#                 commands = commands + p3

#                 robots[2] = i3
#             robots[1] = i2
#         robots[0] = i1

#     total += (len(commands) * int(code[:-1]))
# print(total)

def find_keypad_path2(start, code, path, final):
    if code == '':
        final.append(path)
        return
    
    c = code[0]
    paths = keypad_map[(start, c)]
    for p in paths:
        find_keypad_path2(c, code[1:], path + p + ['A'], final)


total = 0
for code in codes:
    f = []
    find_keypad_path2('A', code, [], f)

    final_commands = []
    for poss in f:
        commands = []
        robots = ['A', 'A']  #robot pointers  
        for i2 in poss:
            start2 = robots[0]
            p2 = find_directional_path((start2, i2), robots[1]) + ['A'] # commands for robot 2
            for i3 in p2:
                start3 = robots[1]
                p3 = find_directional_path((start3, i3), 'A') + ['A'] # commands for robot 3
                commands = commands + p3

                robots[1] = i3
            robots[0] = i2

        final_commands.append(commands)
    
    final_commands.sort(key=len)
    total += (len(final_commands[0]) * int(code[:-1]))
print(total)

    
