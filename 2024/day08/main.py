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
    for char in antennas:
        for node1, node2 in combinations(antennas[char], 2):
            y_diff = abs(node1[1] - node2[1])
            x_diff = abs(node1[0] - node2[0])

            antinode1 = (node1[0] + sign_of(node1[0], node2[0]) * x_diff,
                         node1[1] + sign_of(node1[1], node2[1]) * y_diff)
            antinode2 = (node2[0] + sign_of(node2[0], node1[0]) * x_diff,
                         node2[1] + sign_of(node2[1], node1[1]) * y_diff)

            for x, y in [antinode1, antinode2]:
                if x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines):
                    unique_antinodes.add((x, y))

    print(f"The answer to part one is {len(unique_antinodes)}")


main()
