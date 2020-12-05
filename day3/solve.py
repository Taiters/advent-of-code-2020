# Time: O(NS + S)
# Space: O(S)

from functools import reduce


TREE = '#'
STEPS = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1),
]

def solve(input):
    offsets = [0] * len(STEPS)
    results = [0] * len(STEPS)

    for i, line in enumerate(input):
        for j, step in enumerate(STEPS):
            down, right = step
            if i % down != 0:
                continue

            offset = offsets[j]
            if line[offset % len(line)] == TREE:
                results[j] += 1
            offsets[j] += right

    return reduce(lambda a,b: a*b, results)
