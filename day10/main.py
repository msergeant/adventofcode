def main():
    with open('./input') as file:
        raw = file.read()
        grid = [i for i in raw.strip().split("\n")]

    width = len(grid[0])
    height = len(grid)

    max = 0
    max_coords = (-1, -1)
    for i in range(width):
        for j in range(height):
            if grid[j][i] == '#':
                count = asteroids_in_site(width, height, i, j, grid)
                if count > max:
                    max = count
                    max_coords = (i, j)

    print(max_coords)
    part1 = max
    part2 = -1

    return part1, part2

def asteroids_in_site(width, height, x, y, grid):
    trajectories = set()
    asteroids = 0
    for i in range(width):
        for j in range(height):
            if grid[j][i] == '#' and not (i == x and j == y):
                asteroids += 1
                rise = y - j
                run = x - i
                if rise != 0 and run != 0:
                    denom = gcd(abs(rise), abs(run))
                else:
                    denom = max(abs(rise), abs(run))
                trajectories.add((run // denom, rise // denom))

    return len(trajectories)

def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())

