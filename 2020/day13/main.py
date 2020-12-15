def bus_calc(lines):
    timestamp = int(lines[0])
    times = [int(x) for x in lines[1].split(',') if x != 'x']

    lowest = 999999999999
    id = 0
    for time in times:
        first_available = (timestamp // time) * time + time

        if first_available < lowest:
            id = time
            lowest = first_available

    return (lowest - timestamp) * id

def main():
    with open('./input') as file:
        lines = file.readlines()
        part_one = bus_calc(lines)
        part_two = 0

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

