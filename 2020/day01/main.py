def sum_finder(nums):
    found_sums = {}
    for i in nums:
        if i in found_sums:
            return i * (2020 -i)
        else:
            found_sums[2020 - i] = i

def triplet_finder(nums):
    found_sums = {}
    for i in nums:
        for j in [x for x in nums if i != x]:
            if i in found_sums:
                return found_sums[i] * i
            else:
                found_sums[2020 - i - j] = i * j

def main():
    with open('./input') as file:
        nums = [int(line) for line in file.readlines()]
        part_one = sum_finder(nums)
        part_two = triplet_finder(nums)

        return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
