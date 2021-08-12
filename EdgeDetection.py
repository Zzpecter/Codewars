def group_pairs(values):
    pairs = []
    actual_key = None
    for value in values:
        if not actual_key:
            actual_key = value
        else:
            pairs.append((int(actual_key), int(value)))
            actual_key = None
    return pairs


def build_image(width, value_pairs):
    image = []
    for pair in value_pairs:
        for x in range(pair[1]):
            image.append(pair[0])

    height = len(image)//width
    actual_x = 0
    formatted_image = []
    for h in range(height):
        row = image[actual_x:actual_x+width]
        formatted_image.append(row)
        actual_x += width
    return formatted_image


def calculate_edge_map(image):
    edge_map = []
    for row_index, row in enumerate(image):
        row_edges = []
        for col_index, value in enumerate(row):
            edges = []
            indexes = []
            try:
                edge = value - row[col_index - 1]
                edges.append(edge if edge > 0 else edge * -1)
            except IndexError:
                pass

            if col_index > 0:
                edge = value - row[col_index-1]
                edges.append(edge if edge > 0 else edge*-1)
            if row_index > 0:
                edge = value - image[row_index-1][col_index]
                edges.append(edge if edge > 0 else edge*-1)
            if col_index < len(row) - 1:
                edge = value - row[col_index+1]
                edges.append(edge if edge > 0 else edge*-1)
            if row_index < len(image) - 1:
                edge = value - image[row_index+1][col_index]
                edges.append(edge if edge > 0 else edge*-1)

            if col_index > 0 and row_index > 0:
                edge = value - image[row_index-1][col_index-1]
                edges.append(edge if edge > 0 else edge*-1)
            if col_index > 0 and row_index < len(image) - 1:
                edge = value - image[row_index+1][col_index-1]
                edges.append(edge if edge > 0 else edge*-1)
            if row_index > 0 and col_index < len(row) - 1:
                edge = value - image[row_index-1][col_index+1]
                edges.append(edge if edge > 0 else edge*-1)
            if row_index < len(image) - 1 and col_index < len(row) - 1:
                edge = value - image[row_index+1][col_index+1]
                edges.append(edge if edge > 0 else edge*-1)
            row_edges.append(max(edges))
        edge_map.append(row_edges)
    return edge_map

def edge_detection(image):
    raw_values = image.split(' ')
    width = int(raw_values.pop(0))
    pairs = group_pairs(raw_values)
    image = build_image(width, pairs)
    return calculate_edge_map(image)

image = '7 15 4 100 15 25 2 175 2 25 5 175 2 25 5'
print(edge_detection(image))