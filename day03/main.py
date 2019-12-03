def points_crossed(wire_path):
    vectors = wire_path.split(",")

    position = [0, 0]
    points = []
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
            points.append((position[0] + i * x, position[1] + i * y))

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
                if wire2_points[idx] == point:
                    intersection.append(point)
                    break

                if (wire2_points[idx][0] != point[0] or
                    wire2_points[idx][1] > point[1]):
                    break



    part1 = min(map(lambda x: abs(x[0]) + abs(x[1]), intersection))

    return part1

print("The answer to part 1 is %d\n"
      "The answer to part 2 is " % main())
