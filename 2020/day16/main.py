def sum_invalid_tickets(lines):
    valid_nums = [False for x in range(1000)]
    range_strs = []
    index = 0
    while lines[index]:
        range_strs.extend(lines[index].split(':')[1].split('or'))
        index += 1

    for range_str in range_strs:
        bot, top = [int(x.strip()) for x in range_str.split('-')]
        for i in range(bot, top + 1):
            valid_nums[i] = True

    while lines[index] != "nearby tickets:":
        index += 1

    index += 1

    invalid_total = 0
    while index < len(lines):
        for i in [int(x) for x in lines[index].split(',')]:
            if not valid_nums[i]:
                invalid_total += i

        index += 1

    return invalid_total

def main():
    with open('./input') as file:
        lines = [x.strip() for x in file.readlines()]
        part_one = sum_invalid_tickets(lines)
        part_two = 0

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

