from read_map import read_map
from map_visualization import plot_ground_map

def main():
    filename = 'data/simple.csv'
    result = read_map(filename)
    print(result)
    plot_ground_map(result)

main()