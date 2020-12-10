def mulitply_chain_details(nums):
    valid_chain = [0] + sorted(nums)
    valid_chain.append(valid_chain[-1] + 3)

    one_gaps = 0
    three_gaps = 0
    for i in range(len(valid_chain) - 1):
        diff = valid_chain[i + 1] - valid_chain[i]

        if diff == 3:
            three_gaps += 1
        elif diff == 1:
            one_gaps += 1

    return three_gaps * one_gaps

def count_valid_chains(product, volts, nums, cached_paths):
    if volts in cached_paths:
        return cached_paths[volts]
    else:
        paths_to_this_voltage = []
        for i in range(volts - 3, volts):
            if i in nums:
                paths_to_this_voltage.append(i)

        total_paths = 0
        for path in paths_to_this_voltage:
            to_get_here = count_valid_chains(1, path, nums, cached_paths)
            cached_paths[path] = to_get_here
            total_paths += product * to_get_here

        return total_paths


def main():
    with open('./input') as file:
        nums = [int(x) for x in file.readlines()]
        part_one = mulitply_chain_details(nums)
        max_volts = max(nums) + 3
        part_two = count_valid_chains(1, max_volts, [0] + nums, {0: 1})

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

