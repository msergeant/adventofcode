def twenty_twentieth(nums):
    turn = 1
    vals = {}
    last_num = 0

    while turn <= 2020:
        if turn <= len(nums):
            last_num = nums[turn - 1]
        else:
            if not len(vals[last_num]) > 1:
                last_num = 0
            else:
                last_num = vals[last_num][-1] - vals[last_num][-2]

        vals[last_num] = vals.get(last_num) or []
        vals[last_num].append(turn)
        turn += 1

    return last_num

def main():
    with open('./input') as file:
        nums = [int(x) for x in file.read().split(',')]
        part_one = twenty_twentieth(nums)
        part_two = 0

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

