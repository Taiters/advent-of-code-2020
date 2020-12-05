# Time: O(N)
# Space: O(1)


def parse_line(line):
    options, letter, password = line.strip().split(' ')
    return (
        tuple(int(i) for i in options.split('-')),
        letter[0],
        password
    )


def is_valid(entry):
    options, letter, password = entry
    a, b = options
    if a > len(password):
        return False

    if b > len(password):
        return password[a-1] == letter
    
    return (password[a-1] == letter) ^ (password[b-1] == letter)


def solve(input):
    count = 0
    entries = (parse_line(line) for line in input)
    for entry in entries:
        if is_valid(entry):
            count += 1
    return count
