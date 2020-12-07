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

def shiny_gold_count(lines):
    bag_map = {}
    for line in lines:
        color, rest = line.split("bags ")
        color = color.strip()
        bag_map[color] = {'holds': re.findall(r"\d+ (\w+ \w+) bag", rest)}
        if "shiny gold" in bag_map[color]['holds']:
            bag_map[color]["shiny?"] = True


    shinies = 0
    for bag in bag_map:
        if holds_a_shiny(bag, bag_map):
            shinies += 1

    return shinies

def main():
    with open('./input') as file:
        lines = file.readlines()
        part_one = shiny_gold_count(lines)
        part_two = 0

        return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
