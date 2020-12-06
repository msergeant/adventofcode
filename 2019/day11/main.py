import sys
sys.path.insert(1, '..')
from intcode.computer import IntcodeComputer

def main():
    with open('./input') as file:
        raw = file.read()
        raw_list = [int(i) for i in raw.split(",")]

    program_list = [0] * len(raw_list) * 10

    for i in range(len(raw_list)):
        program_list[i] = raw_list[i]

    comp = IntcodeComputer(program_list)
    position = (0, 0)
    direction = (0, 1)
    colors = {position: 1}
    panels_painted = set()
    while comp.index >= 0:
        color_bit = comp.run_with_input(colors.get(position, 0))
        direction_bit = comp.run()

        colors[position] = color_bit
        if color_bit:
            panels_painted.add(position)

        if direction_bit:
            if direction == (0, 1):
                direction = (1, 0)
            elif direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, -1):
                direction = (-1, 0)
            else:
                direction = (0, 1)
        else:
            if direction == (0, 1):
                direction = (-1, 0)
            elif direction == (1, 0):
                direction = (0, 1)
            elif direction == (0, -1):
                direction = (1, 0)
            else:
                direction = (0, -1)

        position = (position[0] + direction[0], position[1] + direction[1])

    output = []
    for y in range(-10, 10):
        row = []
        for x in range(-10, 80):
            if colors.get((x,y), 0):
                row.append('X')
            else:
                row.append(' ')
        output.append("".join(row))

    output.reverse()
    print("\n".join(output))

main()
