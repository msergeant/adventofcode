def main():
    with open('./input') as file:
        raw = file.read()
        orig = [int(i) for i in raw.strip()]

    nums = orig.copy()
    for _ in range(100):
        nums = [do_phase(i, nums) for i in range(len(nums))]

    part1 = str("".join([str(i) for i in nums[0:8]]))


    offset = int(raw[0:7])

    nums = orig.copy()
    part2_nums = nums[(offset % len(nums)):]
    part2_nums.extend((10000 - offset // len(nums) - 1) * nums)

    for x in range(100):
        part2_nums = do_part2_phase(part2_nums)

    part2 = str("".join([str(i) for i in part2_nums[0:8]]))
    return part1, part2

def do_part2_phase(nums):
    result = nums.copy()
    total = 0
    for i in reversed(range(len(nums))):
        total += nums[i]
        result[i] = total % 10

    return result

def do_phase(pos, nums):
    pattern = get_pattern(pos + 1, len(nums))
    digits = [nums[i] * pattern[i] for i in range(len(nums))]
    return abs(sum(digits)) % 10


def get_pattern(pos, min_length):
    base = [0, 1, 0, -1]
    pattern = []
    for i in base:
        pattern.extend(pos * [i])

    result = pattern.copy()
    while len(result) < min_length + 1:
        result.extend(pattern)

    return result[1:]

print("The answer to part 1 is %s\n"
      "The answer to part 2 is %s" % main())
