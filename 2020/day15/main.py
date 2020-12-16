def turnth(nums, goal):
    turn = 1
    vals = [-1 for i in range(goal + 1)]
    last_num = 0

    hold_num = 0
    while turn <= goal:
        if turn <= len(nums):
            last_num = nums[turn - 1]
        else:
            if hold_num == -1:
                last_num = 0
            else:
                last_num = vals[last_num] - hold_num

        hold_num = vals[last_num]
        vals[last_num] = turn

        turn += 1

    return last_num

def main():
    with open('./input') as file:
        nums = [int(x) for x in file.read().split(',')]
        part_one = turnth(nums, 2020)
        part_two = turnth(nums, 30000000)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

