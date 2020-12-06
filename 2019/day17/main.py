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

    # find_routine(width, height, rows)
    #[L,6,R,12,L,4,L,6,R,6,L,6,R,12,R,6,L,6,R,12,L,6,L,10,L,10,R,6,L,6,R,12,L,4,L,6,R,6,L,6,R,12,L,6,L,10,L,10,R,6,L,6,R,12,L,4,L,6,R,6,L,6,R,12,L,6,L,10,L,10,R,6]
    main = 'B,C,C,A,B,C,A,B,C,A\n'
    a = 'L,6,L,10,L,10,R,6\n'
    b = 'L,6,R,12,L,4,L,6\n'
    c = 'R,6,L,6,R,12\n'

    program_list[0] = 2
    comp = IntcodeComputer(program_list.copy())

    inputs = [
        main,
        a,
        b,
        c,
        'n\n']

    for input in inputs:
        for char in input:
            comp.run_with_input(ord(char))

    part2 = -1
    while comp.index > 0:
        result = comp.run()
        if result > 0:
            part2 = result

    return part1, part2

def find_routine(width, height, rows):
    chrs = [list(rows[i]) for i in range(height)]

    for i in range(1, width):
        for j in range(1, height - 1):
            if rows[j][i] == '^':
                position = (i, j)

    routine = []
    direction = NORTH
    for _ in range(36):
        next_direction = find_next_direction(position, direction, width, height, chrs)
        if next_direction == 'L':
            direction = turn_left(direction)
        else:
            direction = turn_right(direction)
        distance = find_next_distance(position, direction, width, height, chrs)
        for _ in range(distance):
            position = move_forward(position, direction)
        routine.append(next_direction)
        routine.append(distance)
    print(routine)


def turn_right(direction):
    if direction == NORTH:
        return EAST
    elif direction == SOUTH:
        return WEST
    elif direction == EAST:
        return SOUTH
    elif direction == WEST:
        return NORTH

def turn_left(direction):
    for _ in range(3):
        direction = turn_right(direction)
    return direction

def move_forward(position, direction):
    if direction == NORTH:
        return (position[0], position[1] - 1)
    elif direction == SOUTH:
        return (position[0], position[1] + 1)
    elif direction == EAST:
        return (position[0] + 1, position[1])
    elif direction == WEST:
        return (position[0] - 1, position[1])

def find_next_direction(position, direction, width, height, grid):
    right = move_forward(position, turn_right(direction))
    left = move_forward(position, turn_left(direction))

    if(right[0] < 0 or right[0] == width or
       right[1] < 0 or right[1] == height):
        return "L"
    elif grid[right[1]][right[0]] == '#':
        return "R"
    else:
        return "L"

def find_next_distance(position, direction, width, height, grid):
    steps = 0
    position = move_forward(position, direction)
    while(position[0] >= 0 and position[0] < width and
          position[1] >= 0 and position[1] < height and
          grid[position[1]][position[0]] == '#'):
        steps += 1
        position = move_forward(position, direction)

    return steps



print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())

