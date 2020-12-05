# Time: O(n^2)
# Space: O(n)

def solve_for_two(entries, i, total):
    seen = set()
    for i in range(i, len(entries)):
        entry = entries[i]
        if total-entry in seen:
            return (total-entry) * entry
        seen.add(entry)


def solve(input):
    entries = [int(line) for line in input]
    for i, entry in enumerate(entries):
        result = solve_for_two(entries, i+1, 2020-entry)
        if result:
            return entry * result
