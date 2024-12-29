def main():
    list1 = []
    list2 = []
    with open("input", "r") as file:
        for line in file.readlines():
            stripped = line.strip("\n").split("   ")
            num1, num2 = stripped[0], stripped[1]
            list1.append(int(num1))
            list2.append(int(num2))

    list1.sort()
    list2.sort()

    total = 0
    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])

    print(f"The answer to part one is {total}")

    total2 = 0
    for i in range(len(list1)):
        total2 += list2.count(list1[i]) * list1[i]

    print(f"The answer to part two is {total2}")


main()
