
def fuel_counter_upper(mass):
    return mass // 3 - 2


def main():
    with open('./input') as file:
        inputs = file.readlines()
        sum = 0
        for line in inputs:
            sum += fuel_counter_upper(int(line))

        return sum

print(main())
