DIRECTIONS = {
    'E': (1, 0),
    'W': (-1, 0),
    'S': (0, -1),
    'N': (0, 1)
}

class PositionMover():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = 'E'

    def process_command(self, command):
        dir = command[0]
        num = int(command[1:])

        if dir == 'L':
            self.handle_left(num)
        elif dir == 'R':
            self.handle_right(num)
        elif dir == 'F':
            self.handle_move_forward(num)
        else:
            self.handle_move(dir, num)

    def handle_move(self, dir, num):
        i, j = DIRECTIONS.get(dir)

        self.x += i * num
        self.y += j * num

    def handle_move_forward(self, num):
        self.handle_move(self.facing, num)

    def handle_right(self, degrees):
        times = degrees // 90

        for i in range(times):
            if self.facing == 'E':
                self.facing = 'S'
            elif self.facing == 'N':
                self.facing = 'E'
            elif self.facing == 'W':
                self.facing = 'N'
            elif self.facing == 'S':
                self.facing = 'W'

    def handle_left(self, degrees):
        times = degrees // 90

        for i in range(times):
            if self.facing == 'E':
                self.facing = 'N'
            elif self.facing == 'N':
                self.facing = 'W'
            elif self.facing == 'W':
                self.facing = 'S'
            elif self.facing == 'S':
                self.facing = 'E'

class PositionWaypointMover(PositionMover):
    def __init__(self):
        super().__init__()
        self.waypoint_x = 10
        self.waypoint_y = 1

    def handle_move_forward(self, num):
        self.x += self.waypoint_x * num
        self.y += self.waypoint_y * num

    def handle_move(self, dir, num):
        i, j = DIRECTIONS.get(dir)

        self.waypoint_x += i * num
        self.waypoint_y += j * num

    def handle_right(self, degrees):
        times = degrees // 90

        for i in range(times):
            hold = self.waypoint_x
            self.waypoint_x = self.waypoint_y
            self.waypoint_y = hold * -1

    def handle_left(self, degrees):
        times = degrees // 90

        for i in range(times):
            hold = self.waypoint_x
            self.waypoint_x = -1 * self.waypoint_y
            self.waypoint_y = hold


def find_new_distance(lines):
    mover = PositionMover()
    mover2 = PositionWaypointMover()
    for command in lines:
        mover.process_command(command)
        mover2.process_command(command)

    return ((abs(mover.x) + abs(mover.y)),
            (abs(mover2.x) + abs(mover2.y)))

def main():
    with open('./input') as file:
        lines = file.readlines()
        part_one, part_two = find_new_distance(lines)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

