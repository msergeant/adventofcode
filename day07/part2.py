from opcodes import *
from collections import deque
from itertools import permutations

def run_part2(data):
    max = 0
    perm = permutations([9, 8, 7, 6, 5])
    for iter in perm:
        val = single_run(data, iter)
        if val > max:
            max = val

    return max

def single_run(data, setting):
    running_data = [{
        'index': 0,
        'data': data.copy(),
        'inputs': deque([i])}
        for i in setting]

    amp_pointer = 0
    last_result = 0
    running_data[amp_pointer]['inputs'].appendleft(last_result)
    while running_data[4]['index'] >= 0:
        last_result = run_with_feedback(running_data[amp_pointer])
        amp_pointer = (amp_pointer + 1) % 5
        running_data[amp_pointer]['inputs'].appendleft(last_result)

    return running_data[4]['last_result']

def run_with_feedback(program_data):
    index = program_data['index']
    program_list = program_data['data']
    ops = [
        None,
        opcode_1,
        opcode_2,
        opcode_3,
        opcode_4,
        opcode_5,
        opcode_6,
        opcode_7,
        opcode_8,
    ]

    opcode = program_list[index]
    answer = -1
    while index < len(program_list) and opcode != 99:
        if opcode % 10 == 3:
            num = program_data['inputs'].pop()
            offset, _ = opcode_3(index, program_list, num)
        else:
            offset, result = ops[opcode % 10](index, program_list)
        index += offset
        if(opcode % 10 == 4):
            program_data['index'] = index
            program_data['last_result'] = result
            return result
        opcode = program_list[index]


    program_data['index'] = -1
    return -1
