DIRECTIONS = [
    (0, -1),
    (1,  0),
    (0,  1),
    (-1,  0)
]


def would_cause_loop(pos, dir_index, lines):
    visited = set()
    next_x = pos[0] + DIRECTIONS[dir_index][0]
    next_y = pos[1] + DIRECTIONS[dir_index][1]
    fake_block = (next_x, next_y)
    if (next_x >= len(lines[0]) or next_x < 0 or next_y >= len(lines) or next_y < 0):
        return False

    if lines[next_y][next_x] == "#":
        return False

    while (next_x < len(lines[0]) and next_x >= 0 and
           next_y < len(lines) and next_y >= 0):

        if lines[next_y][next_x] == "#" or (next_x, next_y) == fake_block:
            dir_index = (dir_index + 1) % 4

            vector = (pos[0], pos[1], dir_index)
            if vector in visited:
                return True

            visited.add(vector)
        else:
            pos = (next_x, next_y)

        next_x = pos[0] + DIRECTIONS[dir_index][0]
        next_y = pos[1] + DIRECTIONS[dir_index][1]

    return False


def main():
    with open("input") as file:
        lines = []
        for i, line in enumerate(file.readlines()):
            if "^" in line:
                coords = (line.index("^"), i)

            lines.append(line.strip())

    visited = set([coords])
    loopers = set()
    dir_index = 0
    pos = coords
    next_x = pos[0] + DIRECTIONS[dir_index][0]
    next_y = pos[1] + DIRECTIONS[dir_index][1]

    if would_cause_loop(coords, dir_index, lines):
        loopers.add((next_x, next_y))

    while (next_x < len(lines[0]) and next_x >= 0 and
           next_y < len(lines) and next_y >= 0):

        if lines[next_y][next_x] == "#":
            dir_index = (dir_index + 1) % 4
        else:
            pos = (next_x, next_y)

        visited.add(pos)
        next_x = pos[0] + DIRECTIONS[dir_index][0]
        next_y = pos[1] + DIRECTIONS[dir_index][1]

        pos_after = (next_x, next_y)
        if (pos_after not in loopers and
                pos_after not in visited and
                would_cause_loop(pos, dir_index, lines)):
            loopers.add(pos_after)

    print(f"The answer to part one is {len(visited)}")
    print(f"The answer to part two is {len(loopers)}")


main()
