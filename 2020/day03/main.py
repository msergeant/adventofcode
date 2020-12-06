def tree_counter(lines, down=1, right=3):
    x_pos = 0
    trees = 0
    for i, line in enumerate(lines):
        if i % down == 0:
            whole_line = line + line * (x_pos // len(line))
            if whole_line[x_pos] == '#':
                trees += 1
            x_pos += right

    return trees

def all_the_slopes(lines):
    # Right 1, down 1.
    # Right 3, down 1.
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    )

    product = 1
    for right, down in slopes:
        product *= tree_counter(lines, down=down, right=right)

    return product


def main():
    with open('./input') as file:
        lines = [line.strip() for line in file.readlines()]
        part_one = tree_counter(lines)
        part_two = all_the_slopes(lines)

        return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
