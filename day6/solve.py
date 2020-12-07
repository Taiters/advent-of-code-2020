def group_input(input):
    group = []
    for line in input:
        if line:
            group.append(line)
        else:
            yield group
            group = []
    yield group


def count_common(group):
    common = set(list(group[0]))
    for answers in group[1:]:
        common = common.intersection(set(list(answers)))
    return len(common)


def solve(input):
    groups = group_input(input)
    common_total = 0
    for group in groups:
        common_total += count_common(group)
    return common_total
