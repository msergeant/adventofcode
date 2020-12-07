REQUIRED_KEYS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

def count_all_keys_present(entries):
    passports = []
    valid_count = 0
    for entry in entries:
        values = entry.split(" ")
        key_values = [x.split(":") for x in values]
        passport = {k:v for k, v in key_values}
        if all([key in passport for key in REQUIRED_KEYS]):
            valid_count += 1

    return valid_count

def main():
    with open('./input') as file:
        entries = [x.replace('\n', ' ').strip() for x in file.read().split("\n\n")]
        part_one = count_all_keys_present(entries)
        part_two = 0

        return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
