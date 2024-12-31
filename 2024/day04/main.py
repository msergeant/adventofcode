XMAS = "XMAS"
DIRECTIONS = [-1, 0, 1]


def count_xmases(index, line_num, char_num, x_dir, y_dir, lines):
    if index == len(XMAS) - 1 and lines[line_num][char_num] == XMAS[-1:]:
        return 1
    elif lines[line_num][char_num] == XMAS[index]:
        if line_num + y_dir < 0 or char_num + x_dir < 0:
            return 0
        if line_num + y_dir > len(lines) - 1 or char_num + x_dir > len(lines[0]) - 1:
            return 0

        return count_xmases(index + 1, line_num + y_dir, char_num + x_dir, x_dir, y_dir, lines)
    else:
        return 0


def is_xmas(line_num, char_num, lines):
    total = 0
    for line_dir in DIRECTIONS:
        for char_dir in DIRECTIONS:
            if count_xmases(0, line_num, char_num, line_dir, char_dir, lines):
                total += 1

    return total


def is_cross_xmas(line_num, char_num, lines):
    if not (lines[line_num][char_num] == "A" and
            line_num > 0 and
            line_num < len(lines) - 1 and
            char_num > 0 and
            char_num < len(lines[0]) - 1):
        return False

    backslash = set([lines[line_num - 1][char_num - 1], lines[line_num + 1][char_num + 1]])
    forwardslash = set([lines[line_num - 1][char_num + 1], lines[line_num + 1][char_num - 1]])

    return (backslash == {"M", "S"} and
            forwardslash == {"M", "S"})


def main():
    lines = []
    with open("input") as file:
        for line in file.readlines():
            lines.append(line.strip())

    total = 0
    total2 = 0
    for line in range(len(lines)):
        for char in range(len(lines[0])):
            total += is_xmas(line, char, lines)

            if is_cross_xmas(line, char, lines):
                total2 += 1

    print(f"The answer to part one is {total}")
    print(f"The answer to part two is {total2}")


main()
