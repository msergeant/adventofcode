from collections import Counter

def meets_criteria(passwd):
    digits = list(map(lambda x: (passwd // (10**x)) % 10,
                      reversed(range(0,6))))
    doubled = 0
    for i in range(1,6):
        if digits[i] < digits[i-1]:
            return 0
        elif digits[i] == digits[i-1]:
            doubled = 1

    return doubled

def meets_part2_criteria(passwd):
    digits = list(map(lambda x: (passwd // (10**x)) % 10,
                      reversed(range(0,6))))
    return 2 in Counter(digits).values()

def main():
    passing = [i for i in range(125730, 579381) if meets_criteria(i)]
    part1 = len(passing)
    part2 = len([i for i in passing if meets_part2_criteria(i)])
    return part1, part2


print("The answer to part 1 is %d\n"
      "The answer to part 2 is %d" % main())
