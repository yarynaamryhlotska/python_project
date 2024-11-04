def calculate_map_area(ground_map):
    total_area = 0
    lawn_area = 0

    for row in ground_map:
        for cell in row:
            total_area += 1
            if cell == 'L' or cell == 'S':  
                lawn_area += 1

    lawn_percentage = (lawn_area / total_area) * 100 if total_area > 0 else 0

    print(f"Total map area: {total_area} m²")
    print(f"Lawn area: {lawn_area} m²")
    print(f"Lawn area percentage: {lawn_percentage:.2f}%")

    return total_area, lawn_area, lawn_percentage
