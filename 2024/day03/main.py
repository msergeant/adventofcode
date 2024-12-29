import re


def main():
    with open("input") as file:
        matches = re.findall("mul\\(\\d+,\\d+\\)|don't\\(\\)|do\\(\\)", file.read())

        total = 0
        total2 = 0
        ignoring = False
        for match in matches:
            if "don't" in match:
                ignoring = True
            elif "do" in match:
                ignoring = False
            else:
                pairs = [int(x) for x in re.findall("\\d+", match)]
                total += pairs[0] * pairs[1]

                if not ignoring:
                    total2 += pairs[0] * pairs[1]


    print(f"The answer to part one is {total}")
    print(f"The answer to part two is {total2}")


main()
