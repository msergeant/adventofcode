from itertools import permutations
from opcodes import *
from part2 import run_part2

import sys
sys.path.insert(1, '..')
from intcode.computer import IntcodeComputer

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
        comp = IntcodeComputer(program_to_run.copy(), i)
        last_result = comp.run_with_input(last_result)

    return last_result


print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())


