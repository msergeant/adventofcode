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
    blocks = set()
    while comp.index >= 0:
        x = comp.run()
        y = comp.run()
        tile = comp.run()

        if tile == 2:
            blocks.add((x,y))
        elif tile == 4 and (x,y) in blocks:
            blocks.remove((x,y))

    part1 = len(blocks)

    program_list[0] = 2
    comp = IntcodeComputer(program_list)
    blocks = set()
    score = -1
    paddle_x = 10
    ball_x = 0
    ball_y = -1
    joystick = 0
    ball_vector = 1
    last_tile = -1
    while comp.index >= 0:
        if last_tile == 4:
            comp.queue_input(joystick)
        x = comp.run()
        y = comp.run()
        tile = comp.run()

        if tile == 2:
            blocks.add((x,y))
        elif tile == 4 and (x,y) in blocks:
            blocks.remove((x,y))
        elif tile == 3:
            paddle_x = x
            if paddle_x == 34:
                joystick = -1
        elif tile == 4:
            old_vector = ball_vector
            ball_vector = x - ball_x
            ball_x = x
            ball_y = y

            diff = ball_x - paddle_x
            if diff != 0:
                joystick = diff // abs(diff)
            else:
                joystick = 0
        elif x == -1 and y == 0:
            score = tile

        last_tile = tile

    part2 = score

    return part1, part2

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())

