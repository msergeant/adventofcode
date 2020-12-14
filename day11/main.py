FLOOR = 0
OPEN = 1
OCCUPIED = 2

def count_adjacent_taken(x, y, height, width, grid):
    total = 0
    if x > 0 and grid[y][x-1] == OCCUPIED:
        total += 1
    if x < width and grid[y][x+1] == OCCUPIED:
        total += 1
    if y > 0 and grid[y - 1][x] == OCCUPIED:
        total += 1
    if y < height and grid[y + 1][x] == OCCUPIED:
        total += 1

    if y > 0 and x > 0 and grid[y - 1][x - 1] == OCCUPIED:
        total += 1
    if y > 0 and x < width and grid[y - 1][x + 1] == OCCUPIED:
        total += 1
    if y < height and x < width and grid[y + 1][x + 1] == OCCUPIED:
        total += 1
    if y < height and x > 0 and grid[y + 1][x - 1] == OCCUPIED:
        total += 1

    return total

def occupied_after_stabilization(lines):
    current_grid = []

    for line in lines:
        row = []
        for char in line:
            if char == 'L':
                row.append(OPEN)
            elif char == '.':
                row.append(FLOOR)

        current_grid.append(row)

    height = len(lines) - 1
    width  = len(current_grid[0]) - 1

    while True:
        new_grid = []
        occupied_seats = 0
        changed_row = False
        for y in range(len(lines)):
            row = current_grid[y]
            new_row = []
            for x, spot in enumerate(row):
                if spot == FLOOR:
                    new_row.append(FLOOR)
                else:
                    adjacent = count_adjacent_taken(x, y,
                                                    height, width,
                                                    current_grid)

                    if ((spot == OCCUPIED and adjacent < 4) or
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
        part_one = occupied_after_stabilization(lines)
        part_two = 0

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

