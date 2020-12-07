import re


def holds_a_shiny(bag, bag_map):
    if "shiny?" in bag_map[bag]:
        return bag_map[bag].get("shiny?")
    else:
        for color in bag_map[bag]['holds']:
            if holds_a_shiny(color, bag_map):
                bag_map[bag]['shiny?'] = True
                return True

    bag_map[bag]["shiny?"] = False
    return False

def bags_inside(color, bag_map, outer=False):
    holds = bag_map[color]['holds']
    if len(holds) == 0:
        return 1
    else:
        total = 0 if outer else 1
        for subcolor in holds:
            total += holds[subcolor] * bags_inside(subcolor, bag_map)
        return total

def count_the_stuff(lines):
    bag_map = {}
    for line in lines:
        color, rest = line.split("bags ")
        color = color.strip()
        counts = re.findall(r"(\d+ \w+ \w+) bag", rest)
        holds = {}
        for count in counts:
            first_space = count.find(' ')
            num = int(count[0:first_space])
            hold_color = count[first_space+1:]
            holds[hold_color] = num

        bag_map[color] = {'holds': holds}

        if "shiny gold" in bag_map[color]['holds']:
            bag_map[color]["shiny?"] = True

    shinies = 0
    for bag in bag_map:
        if holds_a_shiny(bag, bag_map):
            shinies += 1

    return shinies, bags_inside("shiny gold", bag_map, True)

def main():
    with open('./input') as file:
        lines = file.readlines()
        part_one, part_two = count_the_stuff(lines)

        return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
