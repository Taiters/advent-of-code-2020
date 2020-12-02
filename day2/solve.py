# Time: O(N)
# Space: O(1)

def is_valid(entry):
    options, letter, password = entry
    a, b = options
    if a > len(password):
        return False

    if b > len(password):
        return password[a-1] == letter
    
    return (password[a-1] == letter) ^ (password[b-1] == letter)


def solve(entries):
    count = 0
    for entry in entries:
        if is_valid(entry):
            count += 1
    return count


def parse_line(line):
    options, letter, password = line.strip().split(' ')
    return (
        tuple(int(i) for i in options.split('-')),
        letter[0],
        password
    )


def get_input():
    with open('input.txt', 'r') as f:
        for line in f:
            yield parse_line(line)


if __name__ == '__main__':
    entries = get_input()
    result = solve(entries)
    print(result)
