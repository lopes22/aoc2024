file = open('day9.txt', 'r')
lines = file.readlines()

l = lines[0].strip()

t = 0
l_id = len(l) // 2
l_i = len(l) - 1
f_id = 0
f_i = 0
r = int(l[l_i])
i = 0
while f_id != l_id:
    if i % 2 == 0:
        for j in range(int(l[i])):
            t += f_id * f_i
            f_i += 1
        f_id += 1
    else:
        for j in range(int(l[i])):
            if r > 0:
                t += l_id * f_i
                f_i += 1
                r -= 1
            else:
                l_id -= 1
                l_i -= 2
                r = int(l[l_i])

                if l_id == f_id:
                    break
                else:
                    t += l_id * f_i
                    f_i += 1
                    r -= 1
    i += 1

for k in range(r):
    t += l_id * f_i
    f_i += 1

print(t)






    