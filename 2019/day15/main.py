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
        self.walls = set()
        self.trying_right = True
        self.mapped = False
        self.x_size = [0, 0]
        self.y_size = [0, 0]

    def main(self):
        while not self.completed:
            self.do_step()

        part1 = self.steps

        self.map_unknowns()

        while not self.oxygen_complete:
            self.do_oxygen_step()

        part2 = self.oxygen_steps

        return part1, part2

    def unknowns(self):
        result = []
        for x in range(-19, 20):
            for y in range(-19, 20):
                tst_pos = (x, y)
                if not tst_pos in self.walls and not tst_pos in self.visited:
                    result.append(tst_pos)
        return result

    def map_unknowns(self):
        self.oxygenated = set()
        self.oxygenated.add(self.oxygen_spot)
        self.oxygen_steps = 0
        self.oxygen_complete = False

        for x in range(-19, 20):
            self.walls.add((x, self.y_size[0] + 1))
            self.walls.add((x, self.y_size[1] + 1))
        for y in range(-19, 20):
            self.walls.add((self.x_size[0] - 1, y))
            self.walls.add((self.x_size[1] - 1, y))

        while not self.mapped:
            unk = self.unknowns()

            if len(unk) == 0:
                self.mapped = True
                return None

            adjacent = [NORTH, SOUTH, EAST, WEST]
            go = unk[0]

            if go[0] == self.x_size[0]:
                adjacent.remove(WEST)
            if go[0] == self.x_size[1]:
                adjacent.remove(EAST)
            if go[1] == self.y_size[0]:
                adjacent.remove(NORTH)
            if go[1] == self.y_size[1]:
                adjacent.remove(SOUTH)

            if all([self.next_position(go, x) in self.walls for x in adjacent]):
                self.walls.add(go)
            else:
                self.explore_position(go)

            self.check_mapped()

    def explore_position(self, pos):
        adjacent = [self.next_position(pos, x)
                    for x in [NORTH, SOUTH, EAST, WEST]]
        target = next(x for x in adjacent if x in self.visited)
        if target == self.position:
            target = self.oxygen_spot
        while self.position != target:
            self.do_step()

    def check_mapped(self):
        if len(self.walls) + len(self.visited) >= 1677:
            self.mapped = True

    def do_oxygen_step(self):
        self.oxygen_steps += 1

        for pos in list(self.oxygenated):
            adj = [self.next_position(pos, k) for k in [NORTH, SOUTH, EAST, WEST]]
            for k in adj:
                if k in self.visited:
                    self.oxygenated.add(k)

        if len(self.oxygenated) == len(self.visited):
            self.oxygen_complete = True

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
                self.walls.add(next)
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
                self.oxygen_spot = next
                self.visited[next] = self.steps
                self.position = next
                self.steps += 1
                self.completed = 2
        else:
            result = 0
            self.trying_right = False

        if next[0] < self.x_size[0]:
            self.x_size[0] = next[0]
        if next[1] > self.x_size[1]:
            self.x_size[1] = next[1]

        if next[0] < self.y_size[0]:
            self.y_size[0] = next[0]
        if next[1] > self.y_size[1]:
            self.y_size[1] = next[1]

        return result, next

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

    def next_position(self, position=None, direction=None):
        position = position or self.position
        direction = direction or self.direction
        if direction == NORTH:
            return (position[0], position[1] + 1)
        elif direction == SOUTH:
            return (position[0], position[1] - 1)
        elif direction == EAST:
            return (position[0] + 1, position[1])
        elif direction == WEST:
            return (position[0] - 1, position[1])


print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % Day15Runner().main())

