import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_ground_map(ground_map):
    color_map = {'L': 0, 'O': 1, 'S': 2, 'C': 3, 'E': 2}  

    visual_map = [[color_map[cell] for cell in row] for row in ground_map]

    rows = len(visual_map)
    cols = len(visual_map[0])

    col_map = ListedColormap(['green', 'black', 'yellow', 'red'], 'indexed') 

    plt.figure()
    plt.pcolormesh(visual_map, edgecolors='k', linewidth=2, cmap=col_map)
    ax = plt.gca()
    ax.set_yticks(range(0, rows + 1, 1))
    ax.set_xticks(range(0, cols + 1, 1))
    plt.title(f"Ground Map of size {rows}x{cols}")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.gca().invert_yaxis()
    