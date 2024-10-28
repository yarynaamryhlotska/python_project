import matplotlib.pyplot as plt

def move_visualization(path, initial_x, initial_y, ground_map, start_x, start_y):
    rows = len(ground_map)
    cols = len(ground_map[0])

    fig, ax = plt.subplots(figsize=(8, 8 * rows / cols))  
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal') 
    ax.set_xticks(range(0, cols + 1, 1)) 
    ax.set_yticks(range(0, rows + 1, 1))  
    ax.grid(True, which='both')  
    ax.set_title("Mower Path Visualization")

    plt.xticks(rotation=90)
    plt.tick_params(axis='x', labelsize=8)  
    plt.tick_params(axis='y', labelsize=8)

    ax.plot(initial_x, initial_y, 'bo', label='Start Position')
    
    path_x, path_y = zip(*path)
    ax.plot(path_x, path_y, 'g-', label='Mower Path')
    
    ax.plot(start_x, start_y, 'ro', label='End Position')
    
    plt.legend()
    plt.gca().invert_yaxis()  
