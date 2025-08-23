file = open('day7.txt', 'r')
lines = file.readlines()

equations = []
for line in lines:
    s = line.strip().split(': ')
    t = int(s[0])
    n = list(s[1].split(' '))

    equations.append((t, n))

total = 0
for e in equations:
    q = []

    t = e[0]
    nums = e[1]

    q.append((int(nums[0]) + int(nums[1]), 1))
    q.append((int(nums[0]) * int(nums[1]), 1))
    while len(q) > 0:
        cur = q.pop(0)

        cur_t = cur[0]
        op_c = cur[1]

        if cur_t > t:
            continue

        is_final =  op_c == len(nums) - 1

        if cur_t != t and is_final:
            continue

        if cur_t == t and is_final:
            total += t
            break

        n = nums[op_c + 1]
        q.append((cur_t + int(n), op_c + 1))
        q.append((cur_t * int(n), op_c + 1))

print(total)