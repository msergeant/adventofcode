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

def main():
    part1 = sum(meets_criteria(i) for i in range(125730, 579381))
    return part1


print("The answer to part 1 is %d\n"
      "The answer to part 2 is " % main())
