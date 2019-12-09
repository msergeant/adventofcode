import sys
sys.path.insert(1, '..')
from intcode.computer import IntcodeComputer

def main():
    with open('./input') as file:
        raw = file.read()
        program_list = [int(i) for i in raw.split(",")]

    bigger_list = [0] * len(program_list) * 10

    for i in range(len(program_list)):
        bigger_list[i] = program_list[i]

    comp = IntcodeComputer(bigger_list, 1)
    while comp.index >= 0:
        result = comp.run()
        if comp.index > 1:
            part1 = result

    comp = IntcodeComputer(bigger_list, 2)
    while comp.index >= 0:
        result = comp.run()
        if comp.index > 1:
            part2 = result

    return part1, part2

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())
