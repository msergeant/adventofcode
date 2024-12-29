def is_valid(report):
    diffs = [report[i] - report[i+1] for i in (range(len(report) - 1))]
    signs = set(x > 0 for x in diffs)
    in_range = all(abs(x) >= 1 and abs(x) <= 3 for x in diffs)

    return len(signs) == 1 and in_range


def main():
    reports = []
    with open("input", "r") as file:
        for line in file.readlines():
            stripped = line.strip("\n").split(" ")
            reports.append([int(x) for x in stripped])

    total = 0
    total2 = 0
    for report in reports:
        if is_valid(report):
            total += 1
            total2 += 1
        else:
            for i in range(len(report)):
                if is_valid(report[:i] + report[i + 1:]):
                    total2 += 1
                    break

    print(f"The answer to part one is {total}")
    print(f"The answer to part two is {total2}")


main()
