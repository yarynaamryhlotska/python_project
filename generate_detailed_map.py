def generate_detailed_map(ground_map, N):
    detailed_map = []

    for row in ground_map:
        expanded_row = []
        for cell in row:
            expanded_cell = [cell] * N
            expanded_row.extend(expanded_cell)
        for _ in range(N):
            detailed_map.append(expanded_row.copy())
    
    return detailed_map