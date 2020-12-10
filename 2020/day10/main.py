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

def main():
    with open('./input') as file:
        nums = [int(x) for x in file.readlines()]
        part_one = mulitply_chain_details(nums)
        part_two = 0

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())

