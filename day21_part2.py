
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

            results = [sublist for sublist in all_paths if len(sublist) == min_path]
            directional_map[(s, e)] = results

def find_directional_paths(goal):
    paths = directional_map[goal]

    tpaths = []
    for rpath in paths:
        tcount = 0
        start = goal[0]
        for path_item in rpath:
            if start != path_item:
                tcount += 1
                start = path_item
        tpaths.append((tcount, rpath))

    tpaths.sort()
    t = tpaths[0][0]
    temp = []
    for i in tpaths:
        if i[0] == t:
            temp.append(''.join(i[1]) + 'A')
    return temp


def find_keypad_path2(start, code, path, final):
    if code == '':
        final.append(path)
        return
    
    c = code[0]
    paths = keypad_map[(start, c)]
    for p in paths:
        find_keypad_path2(c, code[1:], path + p + ['A'], final)


c = {}
num = 25
def robot_path(d, p):
    tc = 0    
    pk = (d, p)
    if pk in c:
        return c[pk]

    
    if d == 1:
        cur_pos = 'A'        
        for i in p:
            tc += len(find_directional_paths((cur_pos, i))[0])
            cur_pos = i
        return tc
    else:
        tc = 0
        k = (d, p)
        cur_pos = 'A'
        for i in p:        
            ps = find_directional_paths((cur_pos, i))
            if len(ps) == 0:
                ps = ['A']
            min_c = None
            for new_p in ps:
                rec = robot_path(d - 1, new_p)
                if min_c == None:
                    min_c = rec
                else:
                    min_c = min(rec, min_c)     
            tc += min_c
            cur_pos = i

        c[k] = tc     
        return tc

total = 0


for code in codes:
    print("code", code)
    f = []
    find_keypad_path2('A', code, [], f)

    final_commands = []
    for poss in f:
        print('poss', poss)
        commands = robot_path(num, ''.join(poss))

        final_commands.append(commands)
    
    final_commands.sort()
    total += (final_commands[0] * int(code[:-1]))
print(total)

    
154115708116294
175396398527088