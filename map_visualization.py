import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_ground_map(ground_map, total_area, lawn_area, lawn_percentage):
    color_map = {'O': 0, 'L': 1, 'S': 2, 'C': 3}  

    visual_map = [[color_map[cell] for cell in row] for row in ground_map]

    rows = len(visual_map)
    cols = len(visual_map[0])

    col_map = ListedColormap(['black', 'green',  'yellow', 'red'], 'indexed') 

    plt.figure()
    plt.pcolormesh(visual_map, edgecolors='k', linewidth=2, cmap=col_map)
    ax = plt.gca()
    ax.set_xticks([x + 0.5 for x in range(cols)])
    ax.set_yticks([y + 0.5 for y in range(rows)])
    ax.set_xticklabels(range(0, cols))
    ax.set_yticklabels(range(0, rows))

    plt.title(f"Ground Map of size {rows}x{cols}")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.gca().invert_yaxis()
    
    plt.subplots_adjust(bottom=0.2)  

    plt.figtext(0.5, 0.05, f"Total area: {total_area} m² | Lawn area: {lawn_area} m² | Lawn percentage: {lawn_percentage:.2f}%",
                ha='center', va='top', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
    
    
def plot_ground_detailed_map(ground_map, start_position):
    color_map = {'O': 0, 'L': 1, 'S': 1, 'C': 2}  

    visual_map = [[color_map[cell] for cell in row] for row in ground_map]

    rows = len(visual_map)
    cols = len(visual_map[0])

    col_map = ListedColormap(['black', 'green', 'red'], 'indexed') 

    plt.figure()
    plt.pcolormesh(visual_map, edgecolors='k', linewidth=2, cmap=col_map)
    ax = plt.gca()
        
    ax.set_xticks([x + 0.5 for x in range(cols)])
    ax.set_yticks([y + 0.5 for y in range(rows)])
    ax.set_xticklabels(range(0, cols), fontsize=6)
    ax.set_yticklabels(range(0, rows), fontsize=6)

    plt.title(f"Ground Map of size {rows}x{cols}")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.gca().invert_yaxis()
        
    start_x, start_y = start_position
    plt.plot(start_x + 0.5, start_y + 0.5, 'bo', markersize=8, label='Start Position')


    plt.legend(loc='upper right')
    plt.show()
