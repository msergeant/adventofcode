def parse_seat(seat):
    row_str = seat[0:7].replace('F', '0')
    row_str = row_str.replace('B', '1')
    row = int(row_str, 2)

    col_str = seat[7:].replace('L', '0')
    col_str = col_str.replace('R', '1')
    col = int(col_str, 2)

    return row, col

def seat_id(seat):
    row, col = parse_seat(seat)
    return row * 8 + col

def missing_seats(ids):
    lowest = min(ids)
    highest = max(ids)
    for i in range(lowest, highest):
        if i not in ids:
            return i

    return 0

def main():
    with open('./input') as file:
        lines = file.readlines()
        seat_ids = [seat_id(x) for x in lines]
        part_one = max(seat_ids)
        part_two = missing_seats(seat_ids)

    return part_one, part_two

print("The answer to part 1 is %d\n"
  "The answer to part 2 is %d" % main())
