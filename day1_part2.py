
file = open('day1.txt', 'r')
lines = file.readlines()

total = 0

first = []
second = []
for line in lines:
    line = line.strip()
    split = line.split('   ')

    first.append(int(split[0]))
    second.append(int(split[1]))

times = {}

for n in second:
    if n in times:
        times[n] = times[n] + 1
    else:
        times[n] = 1

for j in first:
    if j in times:
        total += times[j] * j

print(total)