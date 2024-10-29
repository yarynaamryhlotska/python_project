from read_map import read_map
from map_visualization import plot_ground_map
from lawn_mower import find_start_position, mow_lawn
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

    initial_x, initial_y = start_x, start_y
    path = [(initial_x, initial_y)]
    direction = None  

    for _ in range(1650):  
        new_x, new_y, direction = mow_lawn(ground_map, start_x, start_y, direction)
        print(f"Moved to new position: ({new_x}, {new_y}) with direction {direction}")

        path.append((new_x, new_y))
        start_x, start_y = new_x, new_y

    plot_ground_map(ground_map)
    move_visualization(path, initial_x, initial_y, ground_map, start_x, start_y)
    plt.show()
    

main()