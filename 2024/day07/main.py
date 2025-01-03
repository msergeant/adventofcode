from itertools import product


def plus(x, y):
    return x + y


def times(x, y):
    return x * y


def joiner(x, y):
    return int(str(x) + str(y))


OPERS = [plus, times]
PART2_OPERS = [plus, times, joiner]


def process_line(goal, args, operators=OPERS):
    for oper in product(operators, repeat=len(args) - 1):
        acc = args[0]
        for i, arg in enumerate(args[1:]):
            acc = oper[i](acc, arg)

        if acc == goal:
            return True

    return False


def main():
    total = 0
    total2 = 0
    with open("input") as file:
        for line in file.readlines():
            goal, args = line.split(":")
            nums = [int(x) for x in args.strip().split(" ")]
            if process_line(int(goal), nums):
                total += int(goal)
            if process_line(int(goal), nums, PART2_OPERS):
                total2 += int(goal)

    print(f"The answer to part one is {total}")
    print(f"The answer to part two is {total2}")


main()
