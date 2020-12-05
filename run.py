import sys


def get_input(day):
    with open(f'day{day}/input.txt', 'r') as f:
        for line in f:
            yield line.strip()


if __name__ == '__main__':
    day = int(sys.argv[1])
    module = __import__(f'day{day}')
    result = module.solve(get_input(day))
    print(result)
