import random
import math


def find_start_position(ground_map):
    for y in range(len(ground_map) - 1, -1, -1):
        row = ground_map[y]
        for x in range(len(row) - 1, -1, -1):
            if row[x] == 'S':
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

# our solution
# def random_direction(exclude_direction=None):
#     directions = [  
#         (0, 1),  
#         (1, 0),  
#         (0, -1),  
#         (-1, 0), 
#         (1, 1),  
#         (1, -1), 
#         (-1, 1),  
#         (-1, -1)
#     ]
    
#     if exclude_direction:
#         opposite_direction = (-exclude_direction[0], -exclude_direction[1])
#         directions = [d for d in directions if d != opposite_direction]
    
#     return random.choice(directions)

# def mow_lawn(ground_map, x, y, direction=None):
#     if direction is None:
#         direction = random_direction()

#     while True:
#         new_x, new_y = x + direction[0], y + direction[1]

#         if not (0 <= new_x < len(ground_map[0]) and 0 <= new_y < len(ground_map)) or ground_map[new_y][new_x] == 'O':
#             direction = random_direction(exclude_direction=direction)
#             continue

#         if ground_map[y][x] in ['L', 'S', 'E']:  
#             ground_map[y][x] = 'C'

#         x, y = new_x, new_y
#         ground_map[y][x] = 'S'

#         return x, y, direction