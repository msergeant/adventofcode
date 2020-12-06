
def fuel_counter_upper(mass):
    return mass // 3 - 2


def fuel_included_counter(mass):
    sum = 0
    fuel_mass = fuel_counter_upper(mass)
    while fuel_mass >= 0:
        sum += fuel_mass
        fuel_mass = fuel_counter_upper(fuel_mass)

    return sum



def main():
    with open('./input') as file:
        inputs = file.readlines()
        part_one = part_two = 0
        for line in inputs:
            part_one += fuel_counter_upper(int(line))
            part_two += fuel_included_counter(int(line))

        return part_one, part_two

print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())
