from math import radians, sin, cos

LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

ACTIONS = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

def parse_actions(input):
    for line in input:
        letter = line[0]
        value = int(line[1:])
        yield letter, value


def rotate_waypoint(waypoint, value):
    rad = radians(value)
    s = sin(rad)
    c = cos(rad)
    x = round(waypoint[0] * c - waypoint[1] * s)
    y = round(waypoint[0] * s + waypoint[1] * c)
    return [x, y]


def get_location(actions):
    direction = 0
    location = [0, 0]
    waypoint = [10, -1]
    for action, value in actions:
        if action == LEFT or action == RIGHT:
            waypoint = rotate_waypoint(waypoint, value if action == RIGHT else -value)
        elif action == FORWARD:
            location[0] += waypoint[0] * value
            location[1] += waypoint[1] * value
        else:
            waypoint[0] += ACTIONS[action][0] * value
            waypoint[1] += ACTIONS[action][1] * value
    return location


def solve(input):
    actions = parse_actions(input)
    location = get_location(actions)
    return abs(location[0]) + abs(location[1])
