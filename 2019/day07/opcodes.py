def opcode_1(index, program_list):
    (left, right, target) = parse_mode(index, program_list)
    program_list[target] = program_list[left] + program_list[right]
    return 4, program_list[target]

def opcode_2(index, program_list):
    (left, right, target) = parse_mode(index, program_list)
    program_list[target] = program_list[left] * program_list[right]
    return 4, program_list[target]

def opcode_3(index, program_list, num):
    program_list[program_list[index + 1]] = num
    return 2, num

def opcode_4(index, program_list):
    num = parse_mode(index, program_list)[0]
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
    addr_len = min(3, len(program_list) - index - 1)
    return [(index + 1 + i if modes[i] else program_list[index + 1 + i]) for i in range(0,addr_len)]
