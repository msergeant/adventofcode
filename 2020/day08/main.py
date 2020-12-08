def run_instructions(instructions):
    acc = 0
    inst = 0
    visited = []

    while inst < len(instructions):
        if inst in visited:
            return False, acc, visited

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

    return True, acc, visited

def swap_instruction(instruction):
    if instruction[0:3] == "nop":
        return instruction.replace("nop", "jmp")
    else:
        return instruction.replace("jmp", "nop")

def find_bad_line(instructions):
    _, _, inst_list = run_instructions(instructions)

    for index in inst_list:
        inst = instructions[index]
        if not inst[0:3] == "acc":
            instructions[index] = swap_instruction(inst)
            success, acc, _ = run_instructions(instructions)
            if success:
                return acc

            instructions[index] = inst

def main():
    with open('./input') as file:
        lines = file.readlines()
        _, part_one, _ = run_instructions(lines)
        part_two = find_bad_line(lines)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
