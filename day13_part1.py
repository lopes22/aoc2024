import sys
import numpy as np

file = open('day13.txt', 'r')
lines = file.readlines()

cur_line = 0
games = []
while cur_line < len(lines):
    a_sp = lines[cur_line].strip().split(',')
    a = (int(a_sp[0].split('+')[1]), int(a_sp[1].split('+')[1]))

    b_sp = lines[cur_line + 1].strip().split(',')
    b = (int(b_sp[0].split('+')[1]), int(b_sp[1].split('+')[1]))

    p_sp = lines[cur_line + 2].strip().split(',')
    p = (int(p_sp[0].split('=')[1]), int(p_sp[1].split('=')[1]))

    games.append((a, b, p))
    cur_line += 4

t = 0
for g in games:
    a = np.array([[g[0][0], g[1][0]], [g[0][1], g[1][1]]])
    b = np.array([g[2][0], g[2][1]])

    r = np.linalg.solve(a,b).tolist()
    button_a = round(r[0], 2)
    button_b = round(r[1], 2)

    if button_a.is_integer() and button_b.is_integer():
        t += int(button_a) * 3
        t += int(button_b) * 1

print(t)