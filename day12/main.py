from functools import reduce

def parse_planet(line):
    pos =  {val[0].strip(): int(val[1])
            for val in
            ([i.split('=') for i in line.strip('<|>|\n').split(",")])}

    return {'pos': pos, 'vel': {'x': 0, 'y': 0, 'z': 0}}

def handle_gravity(planets):
    for i in range(len(planets)):
        for j in range(len(planets)):
            if i == j:
                break
            single_gravity(planets[i], planets[j])

def single_gravity(planet1, planet2):
    for dir in ['x', 'y', 'z']:
        diff = planet1['pos'][dir] - planet2['pos'][dir]
        if diff != 0:
            diff = diff / abs(diff)

        planet1['vel'][dir] -= diff
        planet2['vel'][dir] += diff

def handle_velocity(planets):
    for planet in planets:
        for dir in ['x', 'y', 'z']:
            planet['pos'][dir] += planet['vel'][dir]

def total_energy(planets):
    total = 0
    for planet in planets:
        kin = 0
        pot = 0
        for dir in ['x', 'y', 'z']:
            kin += abs(planet['vel'][dir])
            pot += abs(planet['pos'][dir])
        total += kin * pot

    return total


def main():
    with open('./input') as file:
        planets = [parse_planet(i) for i in file.readlines()]

    periods = {
        'x': {
            'target': dir_hash(planets, 'x'),
            'period': 0
        },
        'y': {
            'target': dir_hash(planets, 'y'),
            'period': 0
        },
        'z': {
            'target': dir_hash(planets, 'z'),
            'period': 0
        }
    }
    for step in range(1, 200000):
        handle_gravity(planets)
        handle_velocity(planets)
        if step == 1000:
            part1 = total_energy(planets)
        track_periods(periods, planets, step)

    vals = [period['period'] for _, period in periods.items()]
    print(vals)
    part2 = reduce(lcm, vals, 1)

    return part1, part2

def dir_hash(planets, dir):
    return tuple(
        [planets[i][per][dir]
         for per in ['pos', 'vel']
         for i in range(len(planets))])

def track_periods(periods, planets, step):
    for dir in ['x', 'y', 'z']:
        node = periods[dir]
        period = node.get('period', 0)

        if period == 0:
            node['vals'] = node.get('vals', [])
            val_hash = dir_hash(planets, dir)
            if val_hash == node['target']:
                node['period'] = step

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())
