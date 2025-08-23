import sys

file = open('day11.txt', 'r')
lines = file.readlines()

stones = [int(x) for x in lines[0].strip().split(' ')]

c = {}
def blink(s, d):
    if d > 75:
        return 1

    if s == 0:
        return blink(1, d + 1)
    elif len(str(s)) % 2 == 0:
        ss = str(s)
        m = len(ss) // 2
        new_s_1 = int(ss[:m])
        new_s_2 = int(ss[m:])
        r = 0
        if (new_s_1, d) in c:
            r += c[(new_s_1, d)]
        else:
            r1 = blink(new_s_1, d + 1)
            c[(new_s_1, d)] = r1
            r += r1

        if (new_s_2, d) in c:
            r += c[(new_s_2, d)]
        else:
            r2 = blink(new_s_2, d + 1)
            c[(new_s_2, d)] = r2
            r += r2

        return r
    else:
        new_s = s * 2024
        if (new_s, d) in c:
            return c[(new_s, d)]
        else:
            r = blink(new_s, d + 1)
            c[(new_s, d)] = r
            return r

t = 0
for stone in stones:
    t += blink(stone, 1)

print(t)
