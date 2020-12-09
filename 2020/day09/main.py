def find_rogue_number(nums, preamble_length):
    index_map = {num: i for i, num in enumerate(nums)}

    for num in nums[preamble_length:]:
        index = index_map[num]
        found = False
        lookback = index - preamble_length
        for x in range(lookback, index):
            test_num = nums[x]
            diff = num - test_num
            if (diff in index_map and
               index_map[diff] != x
               and index_map[diff] >= lookback):
                found = True
        if not found:
            return num

    return 0


def find_contiguous_set(nums, num):
    index = nums.index(num)

    for test_end in reversed(range(index)):
        for test_begin in reversed(range(test_end)):
            test_region = nums[test_begin:test_end]
            range_sum = sum(test_region)
            if range_sum > num:
                break
            elif range_sum == num:
                range_min = min(test_region)
                range_max = max(test_region)
                return range_max + range_min

def main():
    with open('./input') as file:
        nums = [int(x) for x in file.readlines()]
        part_one = find_rogue_number(nums, 25)
        part_two = find_contiguous_set(nums, part_one)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
