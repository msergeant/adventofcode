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

    for _ in range(1000):
        handle_gravity(planets)
        handle_velocity(planets)

    part1 = total_energy(planets)

    return part1, -1

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())
