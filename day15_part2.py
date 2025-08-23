
file = open('day15.txt', 'r')
lines = file.readlines()

moves = ''
walls = set()
boxes = set()
s_boxes = {}
i = 0
r = 0
start = None
while lines[i] != '\n':
    l = lines[i].strip()

    c = 0
    for s in range(len(l)):
        if l[s] == '@':
            start = (r, c)
        
        if l[s] == '#':
            walls.add((r, c))
            walls.add((r, c + 1))

        if l[s] == 'O':
            boxes.add(((r, c), (r, c + 1)))
            s_boxes[(r,c)] = ((r, c), (r, c + 1))
            s_boxes[(r, c + 1)] = ((r, c), (r, c + 1))

        c += 2

    i += 1
    r += 1

i += 1

while i < len(lines):
    moves += lines[i].strip()

    i += 1

cur = start

def move_box(b, m):
    lb = b[0]
    rb = b[1]
    n_b_l = None
    n_b_r = None
    if m == '^':
        n_b_l = (lb[0] - 1, lb[1])
        n_b_r = (rb[0] - 1, rb[1])
    elif m == 'v':
        n_b_l = (lb[0] + 1, lb[1])
        n_b_r = (rb[0] + 1, rb[1])
    elif m == '<':
        n_b_l = (lb[0], lb[1] - 1)
        n_b_r = (rb[0], rb[1] - 1)
    else:
        n_b_l = (lb[0], lb[1] + 1)
        n_b_r = (rb[0], rb[1] + 1)

    return (n_b_l, n_b_r)

for m in moves:
    n = None
    if m == '^':
        n = (cur[0] - 1, cur[1])
    elif m == 'v':
        n = (cur[0] + 1, cur[1])
    elif m == '<':
        n = (cur[0], cur[1] - 1)
    else:
        n = (cur[0], cur[1] + 1)

    if n in walls:
        continue
    elif n in s_boxes:
        fw = False
        b = s_boxes[n]
        boxes_to_move = []
        boxes_seen = set()
        boxes_to_check = [b]
        while len(boxes_to_check) > 0:
            c_b = boxes_to_check.pop(0)

            if c_b in boxes_seen:
                continue

            boxes_seen.add(c_b)

            n_b = move_box(c_b, m)

            if n_b[0] in walls or n_b[1] in walls:
                fw = True
                break

            if (n_b[0] in s_boxes):
                boxes_to_check.append(s_boxes[n_b[0]])
            
            if (n_b[1] in s_boxes):
                boxes_to_check.append(s_boxes[n_b[1]])

            boxes_to_move.insert(0, (c_b, n_b))

        if fw:
            continue
        else:
            cur = n

            for b_to_move in boxes_to_move:
                old_box = b_to_move[0]
                new_box = b_to_move[1]

                del s_boxes[old_box[0]]
                del s_boxes[old_box[1]]

                s_boxes[new_box[0]] = new_box
                s_boxes[new_box[1]] = new_box

                boxes.remove(old_box)
                boxes.add(new_box)
    else:
        cur = n

t = 0

for fb in boxes:
    b = fb[0]
    t += (100 * b[0]) + b[1]

print(boxes)
print(t)