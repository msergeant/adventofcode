from itertools import product


def plus(x, y):
    return x + y


def times(x, y):
    return x * y


OPERS = [plus, times]


def process_line(goal, args):
    for oper in product(OPERS, repeat=len(args) - 1):
        acc = args[0]
        for i, arg in enumerate(args[1:]):
            acc = oper[i](acc, arg)

        if acc == goal:
            return True

    return False


def main():
    total = 0
    with open("input") as file:
        for line in file.readlines():
            goal, args = line.split(":")
            nums = [int(x) for x in args.strip().split(" ")]
            if process_line(int(goal), nums):
                total += int(goal)

    print(f"The answer to part one is {total}")


main()
