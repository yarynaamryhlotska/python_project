import matplotlib.pyplot as plt

def move_visualization(path, start_x, start_y, ground_map):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.set_xlim(-1, len(ground_map[0]))
    ax.set_ylim(-1, len(ground_map))
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    ax.set_title("Mower Path Visualization")

    ax.plot(start_x, start_y, 'bo', label='Start Position')  

    path_x, path_y = zip(*path)  
    ax.plot(path_x, path_y, 'go-', label='Mower Path')  

    plt.legend()
    plt.gca().invert_yaxis()