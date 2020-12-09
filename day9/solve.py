PREAMBLE_SIZE=25


def get_preamble_set(numbers):
    preamble = set()
    for i in range(0, PREAMBLE_SIZE):
        preamble.add(numbers[i])
    return preamble


def sum_pairs(value, numbers):
    for check in numbers:
        if value - check in numbers:
            return True
    return False


def find_invalid(numbers):
    previous = get_preamble_set(numbers)
    
    for i in range(PREAMBLE_SIZE, len(numbers)):
        value = numbers[i]
        if not sum_pairs(value, previous):
            return value
        previous.remove(numbers[i-PREAMBLE_SIZE])
        previous.add(value)


def find_sum_set(target, numbers):
    start = 0
    end = 0
    current = numbers[0]
    while current != target:
        if current < target:
            end += 1
            current += numbers[end]
        else:
            current -= numbers[start]
            start += 1
    return numbers[start:end+1]
        

def solve(input):
    numbers = [int(i) for i in input]
    invalid = find_invalid(numbers)
    sum_set = find_sum_set(invalid, numbers)
    return min(sum_set) + max(sum_set)
