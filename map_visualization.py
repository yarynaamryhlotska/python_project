import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_ground_map(ground_map):
    visual_map = []
    for row in ground_map:
        visual_row = []
        for cell in row:
            if cell == 'L':
                visual_row.append(0)   
            elif cell == 'O':
                visual_row.append(1)   
            elif cell == 'S':
                visual_row.append(2)   
        visual_map.append(visual_row)

   
    visual_map.reverse()

    
    rows = len(visual_map)
    cols = len(visual_map[0])

   
    col_map = ListedColormap(['green', 'black', 'yellow'], 'indexed')

   
    plt.figure()
    plt.pcolormesh(visual_map, edgecolors='k', linewidth=2, cmap=col_map)

    
    ax = plt.gca()
    ax.set_yticks(range(0, rows + 1, 1))
    ax.set_xticks(range(0, cols + 1, 1))
    plt.title(f"Ground Map of size {rows}x{cols}")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.show()
