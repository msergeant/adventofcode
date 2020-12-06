def opcode_1(index, input):
    (left, right, target) = input[index + 1: index + 4]
    input[target] = input[left] + input[right]

def opcode_2(index, input):
    (left, right, target) = input[index + 1: index + 4]
    input[target] = input[left] * input[right]

def main():
    with open('./input') as file:
        raw = file.read()
        input = [int(i) for i in raw.split(",")]

    # 1202
    part1 = try_pair(12, 2, input)

    target = 19690720
    part2 = -1

    noun = 0
    while part2 < 0 and noun < 100:
        verb = 0
        while part2 < 0 and verb < 100:
            result = try_pair(noun, verb, input)
            if result == target:
                part2 = verb + noun * 100
            verb += 1
        noun += 1

    return part1, part2

def try_pair(noun, verb, initial_data):
    input = initial_data.copy()
    input[1] = noun
    input[2] = verb

    index = 0
    opcode = input[index]
    while opcode != 99:
        if opcode == 1:
            opcode_1(index, input)
        else:
            opcode_2(index, input)
        index += 4
        opcode = input[index]

    return input[0]


print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())
