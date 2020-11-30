#!/usr/bin/env python

from copy import deepcopy

f = open('day02_input.txt', 'r')

opcodes = [int(o) for o in f.readlines()[0].strip().split(',')]
opcodes[1] = 12
opcodes[2] = 2

def part1(opcodes):
    for i in range(0, len(opcodes), 4):
        opcode = opcodes[i]
        if opcode == 99:
            break
        else:
            operand1 = opcodes[opcodes[i+1]]
            operand2 = opcodes[opcodes[i+2]]
            result_index = opcodes[i+3]
            if opcode == 1:
                opcodes[result_index] = operand1 + operand2
            elif opcode == 2:
                opcodes[result_index] = operand1 * operand2
    return opcodes[0]
print(part1(deepcopy(opcodes)))

for i in range(0, len(opcodes)):
    for j in range(0, len(opcodes)):
        opcodes[1] = i
        opcodes[2] = j
        result = part1(deepcopy(opcodes))
        if result == 19690720:
            print(100*i+j)
            exit()
