
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

first.sort()
second.sort()

for i in range(len(first)):
    total += abs(first[i] - second[i])

print(total)