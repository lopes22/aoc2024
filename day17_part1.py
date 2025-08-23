import sys

file = open('day17.txt', 'r')
lines = file.readlines()

reg = {}
reg['A'] = int(lines[0].strip().split(': ')[1])
reg['B'] = int(lines[1].strip().split(': ')[1])
reg['C'] = int(lines[2].strip().split(': ')[1])

instructions = [int(x) for x in lines[4].strip().split(': ')[1].split(',')]

output = []

cur_i = 0

def combo_operand(o):
    if o <= 3:
        return o
    
    if o == 4:
        return reg['A']
    
    if o == 5:
        return reg['B']
    
    if o == 6:
        return reg['C']

while True:
    if cur_i >= len(instructions) - 1:
        break

    cur_opcode = instructions[cur_i]
    cur_operand = instructions[cur_i + 1]

    if cur_opcode == 0:
        v = reg['A'] // (2 ** combo_operand(cur_operand))
        reg['A'] = v

    if cur_opcode == 1:
        v = reg['B'] ^ cur_operand
        reg['B'] = v

    if cur_opcode == 2:
        v = combo_operand(cur_operand) % 8
        reg['B'] = v

    if cur_opcode == 3 and reg['A'] != 0:
        cur_i = cur_operand
        continue

    if cur_opcode == 4:
        v = reg['B'] ^ reg['C']
        reg['B'] = v

    if cur_opcode == 5:
        v = combo_operand(cur_operand) % 8
        output.append(str(v))

    if cur_opcode == 6:
        v = reg['A'] // (2 ** combo_operand(cur_operand))
        reg['B'] = v

    if cur_opcode == 7:
        v = reg['A'] // (2 ** combo_operand(cur_operand))
        reg['C'] = v       
    
    cur_i += 2
        

print(','.join(output))