# Time: O(n^2)
# Space: O(n)

def solve_for_two(entries, i, total):
    seen = set()
    for i in range(i, len(entries)):
        entry = entries[i]
        if total-entry in seen:
            return (total-entry) * entry
        seen.add(entry)


def solve(entries):
    for i, entry in enumerate(entries):
        result = solve_for_two(entries, i+1, 2020-entry)
        if result:
            return entry * result


if __name__ == '__main__':
    entries = []
    with open('input.txt', 'r') as f:
        for line in f:
            entries.append(int(line))

    result = solve(entries)
    print(result)
