def rules_process(rules, update):
    for i, k in enumerate(update):
        if k in rules:
            for v in rules[k]:
                if (v in update and update.index(v) > i):
                    swapped = update
                    swapped[update.index(v)] = k
                    swapped[i] = v
                    good, bad = rules_process(rules, swapped)
                    return 0, max(good, bad)

    return int(update[(len(update) - 1) // 2]), 0


def main():
    rulemode = True
    rules = {}
    total = 0
    total2 = 0
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
                good, bad = rules_process(rules, stripped.split(","))
                total += good
                total2 += bad

    print(f"The answer to part one is {total}")
    print(f"The answer to part two is {total2}")


main()
