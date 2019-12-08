from itertools import permutations
from opcodes import *
from part2 import run_part2

def main():
    with open('./input') as file:
        raw = file.read()
        program_list = [int(i) for i in raw.split(",")]

    max = 0
    perm = permutations([0, 1, 2, 3, 4])
    for iter in perm:
        val = single_run(program_list, iter)
        if val > max:
            max = val

    part1 = max

    part2 = run_part2(program_list)
    return part1, part2

def single_run(program_to_run, phase_setting):
    last_result = 0
    for i in phase_setting:
        program_list = program_to_run.copy()
        last_result = run_with_phase_setting(program_list, (i, last_result))

    return last_result

def run_with_phase_setting(program_list, opcode3_inputs):
    index = 0
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

    opcode = program_list[0]
    answer = -1
    phase_index = 0
    while index < len(program_list) and opcode != 99:
        if opcode % 10 == 3:
            num = opcode3_inputs[phase_index]
            phase_index += 1
            offset, _ = opcode_3(index, program_list, num)
        else:
            offset, result = ops[opcode % 10](index, program_list)
        index += offset
        if(opcode % 10 == 4):
            answer = result
        opcode = program_list[index]


    return answer

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())


