from math import atan2, pi

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

    origin = (23, 19)
    trajectories = sorted_trajectories(width, height, origin[0], origin[1], grid)
    count = 0
    traj_index = 0
    while count < 200:
        traj = trajectories[traj_index]
        x, y = [origin[0] + traj[0], origin[1] + traj[1]]
        while (x >= 0 and
               y >= 0 and
               x < width and
               y < height):
            if grid[y][x] == '#':
                count += 1
                grid[y] = grid[y][:x] + '.' + grid[y][x+1:]
                last = (x,y)
                break
            x, y = [x + traj[0], y + traj[1]]
        traj_index = (traj_index + 1) % len(trajectories)
        traj = trajectories[traj_index]


    print("200th", last)
    part2 = last[0] * 100 + last[1]

    return part1, part2

def angle(point):
    ang = atan2(point[1], point[0])
    ang = pi / 2 + ang
    if ang < 0:
        ang += 2 * pi

    return ang


def sorted_trajectories(width, height, x, y, grid):
    trajectories = set()
    asteroids = 0
    for i in range(width):
        for j in range(height):
            if grid[j][i] == '#' and not (i == x and j == y):
                asteroids += 1
                rise = j - y
                run = i - x
                if rise != 0 and run != 0:
                    denom = gcd(abs(rise), abs(run))
                else:
                    denom = max(abs(rise), abs(run))
                trajectories.add((run // denom, rise // denom))

    all_trajectories = list(trajectories)
    all_trajectories.sort(key=angle)

    return all_trajectories


def asteroids_in_site(width, height, x, y, grid):
    return len(sorted_trajectories(width, height, x, y, grid))

def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())

