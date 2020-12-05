FORWARD = 'F'
LEFT = 'L'
LOWER = {FORWARD, LEFT}


def get_value(low, high, boarding_pass, char_range):
    for index in char_range:
        mid = (low + high) // 2
        direction = boarding_pass[index]
        if direction in LOWER:
            high = mid
        else:
            low = mid
    return low


def get_row(boarding_pass):
    return get_value(0, 128, boarding_pass, range(0, 7))


def get_seat(boarding_pass):
    return get_value(0, 8, boarding_pass, range(7, 10))


def get_seat_ids(boarding_passes):
    for boarding_pass in boarding_passes:
        row = get_row(boarding_pass)
        if row == 0 or row == 127:
            continue

        seat = get_seat(boarding_pass)
        yield row * 8 + seat


def solve(input):
    seat_ids = list(get_seat_ids(input))
    seat_ids.sort()
    for i, id in enumerate(seat_ids):
        if seat_ids[i+1] != id+1:
            return id+1
