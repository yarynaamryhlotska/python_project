import matplotlib.pyplot as plt

def move_visualization(path, initial_x, initial_y, ground_map, start_x, start_y):
    rows = len(ground_map)
    cols = len(ground_map[0])

    fig, ax = plt.subplots(figsize=(8, 8 * rows / cols))  
    ax.set_xlim(0, cols+1)
    ax.set_ylim(0, rows+1)
    ax.set_aspect('equal') 
    ax.set_xticks([x + 0.5 for x in range(cols+1)])  
    ax.set_yticks([y + 0.5 for y in range(rows+1)])  
    ax.set_xticklabels(range(0, cols+1))
    ax.set_yticklabels(range(0, rows+1))
    ax.grid(True, which='both')  
    ax.set_title("Mower Path Visualization")

    plt.xticks(rotation=90)
    plt.tick_params(axis='x', labelsize=8)  
    plt.tick_params(axis='y', labelsize=8)

    ax.plot(initial_x + 1, initial_y + 1, 'bo', label='Start Position')
    
    path_x, path_y = zip(*path)
    ax.plot([x + 1 for x in path_x], [y + 1 for y in path_y], 'g-', label='Mower Path')
    
    ax.plot(start_x + 1, start_y + 1, 'ro', label='End Position')
    
    plt.legend()
    plt.gca().invert_yaxis()  
