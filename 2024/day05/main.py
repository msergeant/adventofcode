def rules_process(rules, update):
    for i, k in enumerate(update):
        if k in rules:
            for v in rules[k]:
                if (v in update and update.index(v) > i):
                    return 0

    return int(update[(len(update) - 1) // 2])


def main():
    rulemode = True
    rules = {}
    total = 0
    with open("input") as file:
        for line in file.readlines():
            stripped = line.strip()
            if stripped == "":
                rulemode = False
            elif rulemode:
                v, k = stripped.split("|")

                if k in rules:
                    rules[k].append(v)
                else:
                    rules[k] = [v]
            else:
                total += rules_process(rules, stripped.split(","))

    print(f"The answer to part one is {total}")


main()
