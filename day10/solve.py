def unique_arrangements(joltages):
    arrangements = [0] * len(joltages)
    arrangements[-1] = 1
    for i in range(len(joltages)-2, -1, -1):
        nextJoltageIndex = i+1
        while nextJoltageIndex < len(joltages):
            difference = joltages[nextJoltageIndex] - joltages[i]
            if difference > 3:
                break
            arrangements[i] += arrangements[nextJoltageIndex]
            nextJoltageIndex += 1
    return arrangements[0]


def solve(input):
    joltages = [int(i) for i in input]
    joltages.append(0)
    joltages.sort()
    return unique_arrangements(joltages)
