FLOOR = 0
OPEN = 1
OCCUPIED = 2

DIRECTIONS = (
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0,  1),
    ( 1,  1),
    ( 1,  0),
    ( 1, -1),
    ( 0, -1),
)

def count_adjacent_taken(x, y, height, width, grid):
    total = 0
    for i, j in DIRECTIONS:
        ex = x + i
        ey = y + j
        if (ex >= 0 and ey >= 0 and ex < width and ey < height and
           grid[ey][ex] == OCCUPIED):
            total += 1

    return total

def count_line_of_sight(x, y, height, width, grid):
    total = 0
    for i, j in DIRECTIONS:
        ex = x + i
        ey = y + j
        while (ex >= 0 and ey >= 0 and ex < width and ey < height):
            if grid[ey][ex] == OCCUPIED:
                total += 1
                break
            elif grid[ey][ex] == OPEN:
                break
            ex += i
            ey += j

    return total

def occupied_after_stabilization(lines, adj_function, target):
    current_grid = []

    for line in lines:
        row = []
        for char in line:
            if char == 'L':
                row.append(OPEN)
            elif char == '.':
                row.append(FLOOR)

        current_grid.append(row)

    height = len(current_grid)
    width  = len(current_grid[0])

    while True:
        new_grid = []
        occupied_seats = 0
        changed_row = False
        for y, row in enumerate(current_grid):
            new_row = []
            for x, spot in enumerate(row):
                if spot == FLOOR:
                    new_row.append(FLOOR)
                else:
                    adjacent = adj_function(x, y,
                                            height, width,
                                            current_grid)

                    if ((spot == OCCUPIED and adjacent < target) or
                       (spot == OPEN and adjacent == 0)):
                        occupied_seats += 1
                        new_row.append(OCCUPIED)
                    else:
                        new_row.append(OPEN)

            if new_row != row:
                changed_row = True

            new_grid.append(new_row)

        if not changed_row:
            return occupied_seats

        current_grid = new_grid

    return -1

def main():
    with open('./input') as file:
        lines = file.readlines()
        part_one = occupied_after_stabilization(lines, count_adjacent_taken, 4)
        part_two = occupied_after_stabilization(lines, count_line_of_sight, 5)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

