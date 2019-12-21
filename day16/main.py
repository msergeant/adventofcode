def main():
    with open('./input') as file:
        raw = file.read()
        nums = [int(i) for i in raw.strip()]

    for _ in range(100):
        nums = [do_phase(i, nums) for i in range(len(nums))]

    part1 = str("".join([str(i) for i in nums[0:8]]))
    return part1, -1

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
      "The answer to part 2 is %d" % main())
