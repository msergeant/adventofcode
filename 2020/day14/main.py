import re


def read_mask(mask):
    or_str = ""
    and_str = ""

    for chr in mask:
        if chr == 'X':
            or_str += '0'
            and_str += '1'
        else:
            or_str += chr
            and_str += chr

    return int(or_str, 2), int(and_str, 2)


def process_input(lines):
    index = 0

    mem = {}
    while index < len(lines):
        if lines[index].startswith("mask"):
            mask = lines[index].split('= ')[1]
            or_val, and_val = read_mask(mask)
            index += 1

            while index < len(lines) and not lines[index].startswith("mask"):
                addr = int(lines[index].split(']')[0][4:])
                val = int(lines[index].split('=')[1])

                val = val | or_val
                val = val & and_val

                mem[addr] = val
                index += 1

    return sum(mem.values())

def main():
    with open('./input') as file:
        lines = [x.strip() for x in file.readlines()]
        part_one = process_input(lines)
        part_two = 0

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

