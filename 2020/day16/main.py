def find_index(num, data):
    every_index_found = True
    for key in data:
        if num in data[key]['valid_indices']:
            data[key]['valid_indices'].remove(num)

        if not data[key].get('index'):
            every_index_found = False

    if every_index_found:
        return None

    for key in data:
        if len(data[key]['valid_indices']) == 1:
            index = list(data[key]['valid_indices'])[0]
            data[key]['index'] = index
            return find_index(index, data)

def process_ticket_info(lines):
    valid_nums = [False for x in range(1000)]
    index = 0

    data = {}
    while lines[index]:
        key = lines[index].split(':')[0].strip()
        range_strs = lines[index].split(':')[1].split('or')
        ranges = []
        for range_str in range_strs:
            bot, top = [int(x.strip()) for x in range_str.split('-')]
            ranges.extend([bot, top])
            for i in range(bot, top + 1):
                valid_nums[i] = True

        data[key] = {
            'ranges': ranges,
            'valid_indices': set(range(20))
        }
        index += 1

    while lines[index] != "your ticket:":
        index += 1

    index += 1

    your_ticket = [int(x.strip()) for x in lines[index].split(',')]

    while lines[index] != "nearby tickets:":
        index += 1

    index += 1

    invalid_total = 0
    while index < len(lines):
        valid_ticket = True
        for i in [int(x) for x in lines[index].split(',')]:
            if not valid_nums[i]:
                valid_ticket = False
                invalid_total += i

        if valid_ticket:
            for i, num in enumerate([int(x) for x in lines[index].split(',')]):
                for key in data:
                    ranges = data[key]['ranges']
                    if num < ranges[0] or (num > ranges[1] and num < ranges[2]):
                        if i in data[key]['valid_indices']:
                            data[key]['valid_indices'].remove(i)

        index += 1

    find_index(-1, data)

    product = 1
    for key in data:
        if "departure" in key:
            product *= your_ticket[data[key]['index']]

    return invalid_total, product

def main():
    with open('./input') as file:
        lines = [x.strip() for x in file.readlines()]
        part_one, part_two = process_ticket_info(lines)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

