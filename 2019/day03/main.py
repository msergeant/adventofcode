def points_crossed(wire_path):
    vectors = wire_path.split(",")

    position = [0, 0]
    points = []
    steps = 1
    for vector in vectors:
        direction = vector[0]
        distance = int(vector[1:])

        if direction == 'R':
            x = 1
            y = 0
        elif direction == 'U':
            x = 0
            y = 1
        elif direction == 'L':
            x = -1
            y = 0
        elif direction == 'D':
            x = 0
            y = -1

        for i in range(1, distance + 1):
            points.append((position[0] + i * x, position[1] + i * y, steps))
            steps += 1

        position[0] = points[-1][0]
        position[1] = points[-1][1]

    return points

def main():
    with open('./input') as file:
        wire1 = file.readline()
        wire2 = file.readline()

    wire1_points = points_crossed(wire1)
    wire2_points = points_crossed(wire2)

    wire1_points.sort()
    wire2_points.sort()

    intersection = []
    wire2_index = {}
    for idx, point in enumerate(wire2_points):
        wire2_index[point[0]] = wire2_index.get(point[0], idx)

    for point in wire1_points:
        start = wire2_index.get(point[0])
        if start:
            for idx in range(start, len(wire2_points)):
                point2 = wire2_points[idx]

                if (point2[0] != point[0] or
                    point2[1] > point[1]):
                    break

                if point2[1] == point[1]:
                    intersection.append((point[0], point[1], point[2] + point2[2]))
                    break

    part1 = min(map(lambda x: abs(x[0]) + abs(x[1]), intersection))
    part2 = min(map(lambda x: x[2], intersection))

    return part1, part2

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())
