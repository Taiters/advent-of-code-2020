def parse_instructions(input):
    for line in input:
        instruction, argument = line.split(' ')
        yield instruction, int(argument)


def run(program):
    i = 0
    acc = 0
    visited = set()
    while i < len(program):
        if i in visited:
            return None

        instruction, argument = program[i]
        visited.add(i)
        if instruction == 'jmp':
            i += argument
            continue

        elif instruction == 'acc':
            acc += argument
        i += 1
    return acc


def solve(input):
    program = list(parse_instructions(input))
    for i in range(len(program)):
        instruction, arg = program[i]
        if instruction in ['jmp', 'nop']:
            program[i] = ('jmp' if instruction == 'nop' else 'nop', arg)
            result = run(program)
            if result:
                return result
            program[i] = (instruction, arg)
    
    return None