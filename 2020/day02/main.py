def password_checker(lines):
    correct = 0
    for line in lines:
        rule, password = line.split(": ")
        limits, char = rule.split(" ")
        min, max = [int(x) for x in limits.split("-")]
        occurs = list(password).count(char)
        if min <= occurs <= max:
            correct += 1

    return correct

def password_checker2(lines):
    correct = 0
    for line in lines:
        rule, password = line.split(": ")
        limits, char = rule.split(" ")
        min, max = [int(x) for x in limits.split("-")]
        if (password[min - 1] == char) ^ (password[max - 1] == char):
            correct += 1

    return correct


def main():
    with open('./input') as file:
        lines = file.readlines()
        part_one = password_checker(lines)
        part_two = password_checker2(lines)

        return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
