import re

REQUIRED_KEYS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

def has_all_keys(passport):
    return all([key in passport for key in REQUIRED_KEYS])

def parse_passport(entry):
    values = entry.split(" ")
    key_values = [x.split(":") for x in values]
    return {k:v for k, v in key_values}

def valid(passport):
    birth = int(passport.get('byr', 0))
    if birth < 1920 or birth > 2002:
        return False

    issue_yr = int(passport.get('iyr', 0))
    if issue_yr < 2010 or issue_yr > 2020:
        return False

    expire_yr = int(passport.get('eyr', 0))
    if expire_yr < 2020 or expire_yr > 2030:
        return False

    hgt = passport.get('hgt', '0cm')
    if re.match("\d+cm$", hgt):
        height = int(hgt.split('cm')[0])
        if height < 150 or height > 193:
            return False
    elif re.match("\d+in$", hgt):
        height = int(hgt.split('in')[0])
        if height < 59 or height > 76:
            return False
    else:
        return False

    hair = passport.get('hcl', '')
    if not re.match("#([0-9]|[a-f]){6}$", hair):
        return False

    eyes = passport.get('ecl', 'nope')
    if eyes not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    if not re.match("\d{9}$", passport.get('pid', '')):
        return False

    return True

def count_valid_passports(entries):
    required_keys_count = 0
    valid_count = 0
    for entry in entries:
        passport = parse_passport(entry)
        if has_all_keys(passport):
            required_keys_count += 1
            if valid(passport):
                valid_count += 1

    return required_keys_count, valid_count

def main():
    with open('./input') as file:
        entries = [x.replace('\n', ' ').strip() for x in file.read().split("\n\n")]
        part_one, part_two = count_valid_passports(entries)

        return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
