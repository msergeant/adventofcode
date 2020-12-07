def sum_unique_group_answers(entries):
    sum = 0
    for entry in entries:
        sum += len(set(entry.replace(' ', '')))

    return sum

def sum_common_answers(entries):
    sum = 0
    for entry in entries:
        subentries = entry.split(' ')
        common = set(subentries[0])
        for sub in subentries[1:]:
            common = common & set(sub)
        sum += len(common)

    return sum


def main():
    with open('./input') as file:
        entries = [x.replace('\n', ' ').strip() for x in file.read().split("\n\n")]
        part_one = sum_unique_group_answers(entries)
        part_two = sum_common_answers(entries)

        return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
