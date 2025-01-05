from itertools import combinations


def sign_of(x, y):
    if x - y > 0:
        return 1
    elif x == y:
        return 0
    else:
        return -1


def main():
    with open("input") as file:
        lines = []
        antennas = {}
        for i, line in enumerate(file.readlines()):
            lines.append(line.strip())

            for j, char in enumerate(line.strip()):
                if char != ".":
                    if char not in antennas:
                        antennas[char] = []

                    antennas[char].append((j, i))

    unique_antinodes = set()
    unique_antinodes_many = set()
    for char in antennas:
        for node1, node2 in combinations(antennas[char], 2):
            y_diff = abs(node1[1] - node2[1])
            x_diff = abs(node1[0] - node2[0])

            unique_antinodes_many.add(node1)
            direction = (sign_of(node1[0], node2[0]) * x_diff,
                         sign_of(node1[1], node2[1]) * y_diff)
            x = node1[0] + direction[0]
            y = node1[1] + direction[1]
            count = 0
            while (x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines)):
                if count == 0:
                    unique_antinodes.add((x, y))
                unique_antinodes_many.add((x, y))
                x += direction[0]
                y += direction[1]
                count += 1

            unique_antinodes_many.add(node2)
            direction = (-direction[0], -direction[1])
            x = node2[0] + direction[0]
            y = node2[1] + direction[1]
            count = 0
            while (x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines)):
                if count == 0:
                    unique_antinodes.add((x, y))
                unique_antinodes_many.add((x, y))
                x += direction[0]
                y += direction[1]
                count += 1

    print(f"The answer to part one is {len(unique_antinodes)}")
    print(f"The answer to part two is {len(unique_antinodes_many)}")


main()
