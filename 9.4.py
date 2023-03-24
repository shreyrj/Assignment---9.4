def convert_coordinates(coordinates):
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)
    updated_coords = [(coord[0] + abs(min_x), coord[1] + abs(min_y)) for coord in coordinates]
    return updated_coords
