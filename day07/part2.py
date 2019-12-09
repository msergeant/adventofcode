from collections import deque
from itertools import permutations

import sys
sys.path.insert(1, '..')
from intcode.computer import IntcodeComputer

def run_part2(data):
    max = 0
    perm = permutations([9, 8, 7, 6, 5])
    for iter in perm:
        val = single_run(data, iter)
        if val > max:
            max = val

    return max

def single_run(data, setting):
    running_data = [
        IntcodeComputer(data.copy(), i)
        for i in setting]

    amp_pointer = 0
    last_result = 0
    while running_data[4].index >= 0:
        last_result = running_data[amp_pointer].run_with_input(last_result)
        amp_pointer = (amp_pointer + 1) % 5

    return running_data[4].current_result
