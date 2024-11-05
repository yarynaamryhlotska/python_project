from read_map import read_map
from map_visualization import plot_ground_map
from lawn_mower import find_start_position, mow_lawn, is_lawn_left
from move_visualization import move_visualization
from map_area_analysis import calculate_map_area  
from plot_percentage_chart import plot_lawn_percentage_chart, plot_cut_uncut_chart
import matplotlib.pyplot as plt


def main():
    filename = 'data/small.csv'
    ground_map = read_map(filename)
    if ground_map is None:
        return

    total_area, lawn_area, lawn_percentage = calculate_map_area(ground_map)

    start_x, start_y = find_start_position(ground_map)
    if start_x is None:
        print("Start position 'S' not found in map.")
        return
    print("Start position:", (start_x, start_y))

    initial_x, initial_y = start_x, start_y
    path = [(initial_x, initial_y)]
    direction = None  

    speed = 0.3
    work_hours = 2
    total_time_seconds = work_hours * 3600 
    max_steps = int(total_time_seconds * speed)  

    for _ in range(max_steps):  
        if not is_lawn_left(ground_map):
            print("All grass has been cut.")
            break
        new_x, new_y, direction = mow_lawn(ground_map, start_x, start_y, direction)
        print(f"Moved to new position: ({new_x}, {new_y}) with direction {direction}")
        path.append((new_x, new_y))
        start_x, start_y = new_x, new_y

    while True:
        print("\nChoose a visualization to display:")
        print("1 - Ground Map Visualization")
        print("2 - Mower Path Visualization")
        print("3 - Lawn Area Percentage Chart")
        print("4 - Cut and Uncut Lawn Area Chart")
        print("0 - Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            plot_ground_map(ground_map, total_area, lawn_area, lawn_percentage)
            plt.show()
        elif choice == '2':
            move_visualization(path, initial_x, initial_y, ground_map, start_x, start_y)
            plt.show()
        elif choice == '3':
            plot_lawn_percentage_chart(lawn_percentage)
            plt.show()
        elif choice == '4':
            plot_cut_uncut_chart(ground_map)
            plt.show()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
