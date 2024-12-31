DIRECTIONS = [
    (0, -1),
    (1,  0),
    (0,  1),
    (-1,  0)
]


def main():
    with open("input") as file:
        lines = []
        for i, line in enumerate(file.readlines()):
            if "^" in line:
                coords = (line.index("^"), i)

            lines.append(line.strip())

    visited = set([coords])
    dir_index = 0
    pos = coords
    next_x = pos[0] + DIRECTIONS[dir_index][0]
    next_y = pos[1] + DIRECTIONS[dir_index][1]

    while (next_x < len(lines[0]) and next_x >= 0 and
           next_y < len(lines) and next_y >= 0):

        if lines[next_y][next_x] == "#":
            dir_index = (dir_index + 1) % 4
        else:
            pos = (next_x, next_y)

        visited.add(pos)
        next_x = pos[0] + DIRECTIONS[dir_index][0]
        next_y = pos[1] + DIRECTIONS[dir_index][1]

    print(f"The answer to part one is {len(visited)}")


main()
