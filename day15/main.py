import sys
sys.path.insert(1, '..')
from intcode.computer import IntcodeComputer

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

class Day15Runner:
    def __init__(self):
        with open('./input') as file:
            raw = file.read()
            raw_list = [int(i) for i in raw.split(",")]

        program_list = [0] * len(raw_list) * 10

        for i in range(len(raw_list)):
            program_list[i] = raw_list[i]

        self.comp = IntcodeComputer(program_list)
        self.position = (0, 0)
        self.direction = EAST
        self.completed = False
        self.steps = 0
        self.visited = {self.position: self.steps}
        self.walls = []
        self.trying_right = True

    def main(self):
        while not self.completed:
            self.do_step()

        part1 = self.steps
        return part1, -1

    def do_step(self):
        if self.trying_right:
            self.turn_right()
        else:
            self.turn_left()

        next = self.next_position()
        result = -1
        if not next in self.walls:
            result = self.comp.run_with_input(self.direction)
            if result == 0:
                self.walls.append(next)
                self.trying_right = False
                return result, next
            elif result == 1:
                self.trying_right = True
                if self.visited.get(next):
                    self.steps = self.visited.get(next)
                    self.position = next
                else:
                    self.steps += 1
                    self.visited[next] = self.steps
                    self.position = next
            elif result == 2:
                self.steps += 1
                self.completed = 2
        else:
            self.trying_right = False

        return result, self.position

    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == WEST:
            self.direction = NORTH

    def turn_left(self):
        for _ in range(3):
            self.turn_right()

    def next_position(self):
        if self.direction == NORTH:
            return (self.position[0], self.position[1] + 1)
        elif self.direction == SOUTH:
            return (self.position[0], self.position[1] - 1)
        elif self.direction == EAST:
            return (self.position[0] + 1, self.position[1])
        elif self.direction == WEST:
            return (self.position[0] - 1, self.position[1])


print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % Day15Runner().main())

