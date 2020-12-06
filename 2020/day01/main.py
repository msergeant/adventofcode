def sum_finder(nums):
    found_sums = {}
    for i in nums:
        if i in found_sums:
            return i * (2020 -i)
        else:
            found_sums[2020 - i] = i

def main():
    with open('./input') as file:
        nums = [int(line) for line in file.readlines()]
        part_one = sum_finder(nums)

        return part_one, 0

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
