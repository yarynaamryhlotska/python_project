import matplotlib.pyplot as plt

def move_visualization(path, start_x, start_y, ground_map):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Налаштування меж графіку на основі розмірів карти
    ax.set_xlim(-1, len(ground_map[0]))
    ax.set_ylim(-1, len(ground_map))
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    ax.set_title("Mower Path Visualization")

    # Відображення початкової позиції косарки
    ax.plot(start_x, start_y, 'bo', label='Start Position')  # синя точка - стартова позиція

    # Відображення траєкторії косарки
    path_x, path_y = zip(*path)  # Розпаковуємо координати шляху на x і y
    ax.plot(path_x, path_y, 'go-', label='Mower Path')  # зелена лінія з точками - траєкторія косарки

    # Додаємо легенду та показуємо графік
    plt.legend()
   
