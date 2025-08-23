import sys

file = open('day11.txt', 'r')
lines = file.readlines()

stones = [int(x) for x in lines[0].strip().split(' ')]

for blink in range(75):
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == 0:
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            s = str(stones[i])
            m = len(s) // 2
            new_stones.append(int(s[:m]))
            new_stones.append(int(s[m:]))
        else:
            new_stones.append(stones[i] * 2024)
    
    stones = new_stones

print(len(stones))
