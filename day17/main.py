import sys
sys.path.insert(1, '..')
from intcode.computer import IntcodeComputer

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

def main():
    with open('./input') as file:
        raw = file.read()
        raw_list = [int(i) for i in raw.split(",")]

    program_list = [0] * len(raw_list) * 10

    for i in range(len(raw_list)):
        program_list[i] = raw_list[i]

    comp = IntcodeComputer(program_list.copy())
    output = []
    while comp.index >= 0:
        result = comp.run()
        if(comp.index > 0):
            output.append(chr(result))

    output = ("".join(output)).strip()

    rows = output.split("\n")
    width = len(rows[0])
    height = len(rows)

    intersections = []
    surroundings = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if rows[j][i] == '#':
                if all([rows[y + j][x + i] == '#' for x, y in surroundings]):
                    intersections.append((i, j))

    part1 = sum([x * y for x,y in intersections])

    return part1, -1

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())

