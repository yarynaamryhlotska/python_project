import random
import math


def find_start_position(ground_map):
    for y, row in enumerate(ground_map):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y
    return None


def random_direction():
    angle = random.uniform(0, 2 * math.pi) 
    x = math.cos(angle)
    y = math.sin(angle)
    return (x, y) 


def is_lawn_left(ground_map):
    for row in ground_map:
        if 'L' in row:
            return True
    return False


def mow_lawn(ground_map, x, y, direction=None):
    if direction is None:
        direction = random_direction()

    while True:
        # Changed new position x and y
        new_x, new_y = x + direction[0], y + direction[1]
        new_x_int, new_y_int = round(new_x), round(new_y)

        if not (0 <= new_x_int < len(ground_map[0]) and 0 <= new_y_int < len(ground_map)) or ground_map[new_y_int][new_x_int] == 'O':
            direction = random_direction()
            continue

        if ground_map[round(y)][round(x)] in ['L', 'S']:
            ground_map[round(y)][round(x)] = 'C' 

        x, y = new_x, new_y
        ground_map[new_y_int][new_x_int] = 'C' 

        return x, y, direction  

