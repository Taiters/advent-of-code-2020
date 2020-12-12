EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'
ADJACENT = [
    (0, 1),  # RIGHT
    (1, 0),  # DOWN
    (1, 1),  # DOWN/RIGHT
    (1, -1), # DOWN/LEFT
]


def valid_coords(seats, row, col):
    return row >= 0 and row < len(seats) and col >= 0 and col < len(seats[0])


def count_adjacent(seats, seat_lookup, row, col):
    count = 0
    for r, c in seat_lookup[(row, col)]:
        if seats[r][c] == OCCUPIED:
            count += 1
    return count


def seating_pass(seats, seat_lookup):
    updates = []
    for row in range(0, len(seats)):
        for col in range(0, len(seats[0])):
            seat = seats[row][col]
            if seat == FLOOR:
                continue

            adjacent = count_adjacent(seats, seat_lookup, row, col)
            if seat == EMPTY and adjacent == 0:
                updates.append((row, col))
            elif seat == OCCUPIED and adjacent >= 5:
                updates.append((row, col))
    
    for row, col in updates:
        seat = seats[row][col]
        seats[row][col] = OCCUPIED if seat == EMPTY else EMPTY
    
    return len(updates)


def count_occupied(seats):
    count = 0
    for row in range(0, len(seats)):
        for col in range(0, len(seats[0])):
            if seats[row][col] == OCCUPIED:
                count += 1
    return count


def find_in_direction(seats, direction, row, col):
    check_row = row + direction[0]
    check_col = col + direction[1]
    while valid_coords(seats, check_row, check_col) and seats[check_row][check_col] != EMPTY:
        check_row += direction[0]
        check_col += direction[1]
    return (check_row, check_col) if valid_coords(seats, check_row, check_col) else None


def find_adjacent_seats(seats, row, col):
    adjacent = []
    for direction in ADJACENT:
        seat = find_in_direction(seats, direction, row, col)
        if seat is not None:
            adjacent.append(seat)
    return adjacent


def build_seat_lookup(seats):
    lookup = {}
    for row in range(0, len(seats)):
        for col in range(0, len(seats[0])):
            if seats[row][col] != EMPTY:
                continue

            adjacent_seats = find_adjacent_seats(seats, row, col)
            if (row, col) not in lookup:
                lookup[(row, col)] = set()
            
            for seat in adjacent_seats:
                lookup[(row, col)].add(seat)
                if seat not in lookup:
                    lookup[seat] = set()
                lookup[seat].add((row, col))
    return lookup


def solve(input):
    seats = [list(line) for line in input]
    seat_lookup = build_seat_lookup(seats)

    updates = float('Inf')
    while updates > 0:
        updates = seating_pass(seats, seat_lookup)
    return count_occupied(seats)
