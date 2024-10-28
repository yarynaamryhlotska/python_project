from read_map import read_map
from map_visualization import plot_ground_map
from lawn_mower import find_start_position, random_bounce_velocity, mow_lawn, random_direction
from move_visualization import move_visualization
import matplotlib.pyplot as plt


def main():
    filename = 'data/small.csv'
    ground_map = read_map(filename)
    if ground_map is None:
        return

    start_x, start_y = find_start_position(ground_map)
    if start_x is None:
        print("Start position 'S' not found in map.")
        return
    print("Start position:", (start_x, start_y))

    current_direction = random_direction()
    path = []  

    for _ in range(200):  
        if ground_map[start_y][start_x] == 'S':
            ground_map[start_y][start_x] = 'C'
        elif ground_map[start_y][start_x] == 'E':  
            ground_map[start_y][start_x] = 'C'
        
        new_x, new_y, current_direction = mow_lawn(ground_map, start_x, start_y)
        print(f"Moved to new position: ({new_x}, {new_y}) with direction {current_direction}")

        path.append((new_x, new_y))
        start_x, start_y = new_x, new_y
    plot_ground_map(ground_map)
    move_visualization(path, start_x, start_y, ground_map)
    plt.show()
    

main()