import random
import math


def find_start_position(ground_map):
    for y, row in enumerate(ground_map):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y
    return None


def next_step(x, y, vx, vy, delta_t):
    new_x = x + vx * delta_t
    new_y = y + vy * delta_t
    
    return new_x, new_y


def random_bounce_velocity(v):
    angle = random.uniform(0, 2 * math.pi)
    vx = v * math.cos(angle)
    vy = v * math.sin(angle)
    return vx, vy


def random_direction(exclude_direction=None):
    directions = [
        (0, 1),  
        (1, 0),  
        (0, -1),  
        (-1, 0), 
        (1, 1),  
        (1, -1), 
        (-1, 1),  
        (-1, -1)  
    ]
    
    if exclude_direction:
        directions = [d for d in directions if (d[0], d[1]) != (-exclude_direction[0], -exclude_direction[1])]
    
    return random.choice(directions)


def mow_lawn(ground_map, x, y):
    direction = random_direction()  
    
    while True:
        new_x, new_y = x + direction[0], y + direction[1]

        if not (0 <= new_x < len(ground_map[0]) and 0 <= new_y < len(ground_map)) or ground_map[new_y][new_x] == 'O':
            direction = random_direction(exclude_direction=direction)
            continue  

        if ground_map[y][x] in ['L', 'S', 'E']:  
            ground_map[y][x] = 'C'

        x, y = new_x, new_y

        ground_map[y][x] = 'E'

        return x, y, direction
