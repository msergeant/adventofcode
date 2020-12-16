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

def addresses(mask):
    if 'X' in mask:
        return (addresses(re.sub('X', '1', mask, 1)) +
                addresses(re.sub('X', '0', mask, 1)))
    else:
        return [int(mask, 2)]

def find_floats(addr, mask):
    new_mask = ''
    for i, chr in enumerate(mask):
        if chr == 'X':
            new_mask += chr
        elif chr == '1' or (addr & (2 ** (35 - i))):
            new_mask += '1'
        else:
            new_mask += '0'

    return(addresses(new_mask))


def process_input(lines):
    index = 0

    mem = {}
    mem2 = {}
    while index < len(lines):
        if lines[index].startswith("mask"):
            mask = lines[index].split('= ')[1]
            or_val, and_val = read_mask(mask)
            index += 1

            while index < len(lines) and not lines[index].startswith("mask"):
                addr = int(lines[index].split(']')[0][4:])
                val = int(lines[index].split('=')[1])
                val2 = val

                val = val | or_val
                val = val & and_val

                mem[addr] = val

                # part 2
                addrs = find_floats(addr, mask)
                for a in addrs:
                    mem2[a] = val2

                index += 1

    return sum(mem.values()), sum(mem2.values())

def main():
    with open('./input') as file:
        lines = [x.strip() for x in file.readlines()]
        part_one, part_two = process_input(lines)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

