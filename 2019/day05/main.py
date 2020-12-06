def opcode_1(index, program_list):
    (left, right, target) = parse_mode(index, program_list)
    program_list[target] = program_list[left] + program_list[right]
    return 4, program_list[target]

def opcode_2(index, program_list):
    (left, right, target) = parse_mode(index, program_list)
    program_list[target] = program_list[left] * program_list[right]
    return 4, program_list[target]

def opcode_3(index, program_list):
    num = int(input("1 for part 1; 5 for part 2: "))
    program_list[program_list[index + 1]] = num
    return 2, num

def opcode_4(index, program_list):
    (num, _, _) = parse_mode(index, program_list)
    print("op4", index, program_list[num])
    return 2, program_list[num]

def opcode_5(index, program_list):
    (tst, addr, _) = parse_mode(index, program_list)
    if program_list[tst]:
        return program_list[addr] - index, -1
    else:
        return 3, -1

def opcode_6(index, program_list):
    (tst, addr, _) = parse_mode(index, program_list)
    if program_list[tst]:
        return 3, -1
    else:
        return program_list[addr] - index, -1

def opcode_7(index, program_list):
    (left, right, target) = parse_mode(index, program_list)
    if program_list[left] < program_list[right]:
        program_list[target] = 1
    else:
        program_list[target] = 0
    return 4, -1

def opcode_8(index, program_list):
    (left, right, target) = parse_mode(index, program_list)
    if program_list[left] == program_list[right]:
        program_list[target] = 1
    else:
        program_list[target] = 0
    return 4, -1

def parse_mode(index, program_list):
    command = program_list[index]
    modes = [(command // 10**(x+2)) % 10 for x in range(0,3)]
    return [(index + 1 + i if modes[i] else program_list[index + 1 + i]) for i in range(0,3)]

def main():
    with open('./input') as file:
        raw = file.read()
        program_list = [int(i) for i in raw.split(",")]

    index = 0
    ops = [
        None,
        opcode_1,
        opcode_2,
        opcode_3,
        opcode_4,
        opcode_5,
        opcode_6,
        opcode_7,
        opcode_8,
    ]

    opcode = program_list[0]
    answer = -1
    while index < len(program_list) and opcode != 99:
        offset, result = ops[opcode % 10](index, program_list)
        index += offset
        if(opcode % 10 == 4):
            answer = result
        opcode = program_list[index]


    return answer

print("The answer is %d" % main())


