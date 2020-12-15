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

def earliest_timestamp(lines):
    times = {int(x): k for k, x in enumerate(lines[1].split(',')) if x != 'x'}

    comparator = 1
    for num in times:
        comparator *= num

    reduce_by = 1

    while True:
        done = True
        for num, offset in times.items():
            if (comparator + offset) % num == 0:
                if reduce_by % num != 0:
                    reduce_by *= num
            else:
                done = False

        if done:
            return comparator

        comparator -= reduce_by

    return 0

def main():
    with open('./input') as file:
        lines = file.readlines()
        part_one = bus_calc(lines)
        part_two = earliest_timestamp(lines)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

