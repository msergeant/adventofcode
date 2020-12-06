from collections import deque


class IntcodeComputer:
    def __init__(self, program, initial_input = None):
        self.program = program
        self.input_queue = deque()
        if initial_input != None:
            self.input_queue.appendleft(initial_input)
        self.index = 0
        self.relative_index = 0
        self.current_result = None

    def queue_input(self, num):
        self.input_queue.appendleft(num)

    def opcode_1(self, index):
        (left, right, target) = self.parse_mode(index)
        self.program[target] = self.program[left] + self.program[right]
        return 4, self.program[target]

    def opcode_2(self, index):
        (left, right, target) = self.parse_mode(index)
        self.program[target] = self.program[left] * self.program[right]
        return 4, self.program[target]

    def opcode_3(self, index):
        num = self.input_queue.pop()
        addr = self.parse_mode(index)[0]
        self.program[addr] = num
        return 2, num

    def opcode_4(self, index):
        num = self.parse_mode(index)[0]
        return 2, self.program[num]

    def opcode_5(self, index):
        (tst, addr, _) = self.parse_mode(index)
        if self.program[tst]:
            return self.program[addr] - index, -1
        else:
            return 3, -1

    def opcode_6(self, index):
        (tst, addr, _) = self.parse_mode(index)
        if self.program[tst]:
            return 3, -1
        else:
            return self.program[addr] - index, -1

    def opcode_7(self, index):
        (left, right, target) = self.parse_mode(index)
        if self.program[left] < self.program[right]:
            self.program[target] = 1
        else:
            self.program[target] = 0
        return 4, -1

    def opcode_8(self, index):
        (left, right, target) = self.parse_mode(index)
        if self.program[left] == self.program[right]:
            self.program[target] = 1
        else:
            self.program[target] = 0
        return 4, -1

    def opcode_9(self, index):
        num = self.parse_mode(index)[0]
        self.relative_index += self.program[num]
        return 2, -1

    def parse_mode(self, index):
        command = self.program[index]
        modes = [(command // 10**(x+2)) % 10 for x in range(0,3)]
        addr_len = min(3, len(self.program) - index - 1)
        return [self.find_index(modes[i], index + 1 + i) for i in range(0,addr_len)]

    def find_index(self, mode, addr):
        if mode == 1:
            return addr
        elif mode == 2:
            return self.relative_index + self.program[addr]
        else:
            return self.program[addr]

    def run_with_input(self, num):
        self.queue_input(num)
        return self.run()

    def run(self):
        local_index = self.index
        ops = [
            None,
            self.opcode_1,
            self.opcode_2,
            self.opcode_3,
            self.opcode_4,
            self.opcode_5,
            self.opcode_6,
            self.opcode_7,
            self.opcode_8,
            self.opcode_9
        ]

        opcode = self.program[local_index]
        answer = -1
        while 0 <= local_index < len(self.program) and opcode != 99:
            offset, result = ops[opcode % 10](local_index)
            local_index += offset
            if(opcode % 10 == 4):
                self.index = local_index
                self.current_result = result
                return result
            opcode = self.program[local_index]


        self.index = -1
        return -1
