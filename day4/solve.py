import sys
import re
from functools import partial


EXPECTED_KEYS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

def in_range(min, max, value):
    value = int(value)
    return value >= min and value <= max

def valid_height(height):
    match = re.match('^(\d+)(in|cm)', height)
    if match:
        value = int(match[1])
        unit = match[2]
        if unit == 'in':
            return value >= 59 and value <= 76
        return value >=150 and value <= 193
    return False

validators = {
    'byr': partial(in_range, 1920, 2002),
    'iyr': partial(in_range, 2010, 2020),
    'eyr': partial(in_range, 2020, 2030),
    'hgt': valid_height,
    'hcl': partial(re.match, '^#[0-9a-f]{6}$'),
    'ecl': lambda v: v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': partial(re.match, '^\d{9}$'),
}

def parse_passports(input):
    current_passport = {}
    for line in input:
        if line:
            pairs = line.split(' ')
            for k, v in (p.split(':') for p in pairs):
                current_passport[k] = v
        else:
            yield current_passport
            current_passport = {}
    yield current_passport


def is_valid(passport):
    for key in EXPECTED_KEYS:
        if key not in passport or not validators[key](passport[key]):
            return False
    return True


def solve(input):
    valid = 0
    passports = parse_passports(input)
    for passport in passports:
        if is_valid(passport):
            valid += 1
    return valid
