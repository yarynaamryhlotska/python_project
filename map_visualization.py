import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_ground_map(ground_map, total_area, lawn_area, lawn_percentage):
    color_map = {'L': 0, 'O': 1, 'S': 2, 'C': 3, 'E': 2}  

    visual_map = [[color_map[cell] for cell in row] for row in ground_map]

    rows = len(visual_map)
    cols = len(visual_map[0])

    col_map = ListedColormap(['green', 'black', 'yellow', 'red'], 'indexed') 

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
    
    # Adjust layout to create space at the bottom for the text
    plt.subplots_adjust(bottom=0.2)  # Adds extra space at the bottom

    # Adding text for area information below the plot
    plt.figtext(0.5, 0.05, f"Total area: {total_area} m² | Lawn area: {lawn_area} m² | Lawn percentage: {lawn_percentage:.2f}%",
                ha='center', va='top', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
