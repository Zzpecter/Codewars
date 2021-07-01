def get_next_direction(actual_direction):
    directions = ['RIGHT', 'DOWN', 'LEFT', 'UP']
    actual_index = directions.index(actual_direction)
    if actual_index == len(directions) - 1:
        return directions[0]
    return directions[actual_index+1]


def move_index(index_y, index_x, direction, traversed_array):
    if direction == 'UP':
        if index_y - 1 < 0 or traversed_array[index_y - 1][index_x]:
            direction = get_next_direction(direction)
            return move_index(index_y, index_x, direction, traversed_array)
        else:
            index_y -= 1
    elif direction == 'DOWN':
        if index_y + 1 >= len(traversed_array) or traversed_array[index_y + 1][index_x]:
            direction = get_next_direction(direction)
            return move_index(index_y, index_x, direction, traversed_array)
        else:
            index_y += 1
    elif direction == 'LEFT':
        if index_x - 1 < 0 or traversed_array[index_y][index_x - 1]:
            direction = get_next_direction(direction)
            return move_index(index_y, index_x, direction, traversed_array)
        else:
            index_x -= 1
    elif direction == 'RIGHT':
        if index_x+1 >= len(traversed_array[0]) or traversed_array[index_y][index_x + 1]:
            direction = get_next_direction(direction)
            return move_index(index_y, index_x, direction, traversed_array)
        else:
            index_x += 1
    return index_y, index_x, direction


def snail(snail_map):

    traversed_array = [[False for i in range(len(snail_map))] for i in range(len(snail_map[0]))]

    output_array = []

    if len(snail_map[0]) > 0:
        index_y, index_x = 0, 0
        current_direction = 'RIGHT'
        output_array.append(snail_map[index_y][index_x])
        traversed_array[index_y][index_x] = True

        while not all([item for sublist in traversed_array for item in sublist]):
            index_y, index_x, current_direction = move_index(index_y, index_x, current_direction, traversed_array)
            output_array.append(snail_map[index_y][index_x])
            traversed_array[index_y][index_x] = True

    return output_array

array = [[]]

print(snail(array))