def first_repeated_instruction(instructions):
    acc = 0
    inst = 0
    visited = []

    while inst < len(instructions):
        if inst in visited:
            return acc

        visited.append(inst)

        oper, amount = instructions[inst].split(" ")
        sign = 1 if amount[0] == '+' else -1
        amount = int(amount[1:]) * sign

        if oper == "jmp":
            inst += amount
        else:
            inst += 1

        if oper == "acc":
            acc += amount

    return 0


def main():
    with open('./input') as file:
        lines = file.readlines()
        part_one = first_repeated_instruction(lines)
        part_two = 0

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
