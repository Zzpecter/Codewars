DIRECTIONS = ['RIGHT', 'DOWN', 'LEFT', 'UP']


def detect_collision(index_y, index_x, direction, spiral):
    if direction == 'RIGHT':
        if index_x + 1 > len(spiral[0]):
            return False
        if index_x + 2 < len(spiral[0]) and spiral[index_y][index_x+1] == 1:
            return False

    elif direction == 'DOWN':
        if index_y + 1 > len(spiral):
            return False
        if index_y + 2 < len(spiral) and spiral[index_y+1][index_x] == 1:
            return False

    elif direction == 'LEFT':
        if index_x < 0:
            return False
        if index_x - 2 >= 0 and spiral[index_y][index_x-1] == 1:
            return False

    elif direction == 'UP':
        if index_y < 0:
            return False
        elif index_y - 1 >= 0 and spiral[index_y-1][index_x] == 1:
            return False
    return True

def spiralize(size):
    current_dir_index = 0
    empty_spiral = []
    for i in range(size):
        empty_spiral.append([0]*size)

    row_idx, col_idx = 0, 0
    last_move = True

    for row in range(size):
        for col in range(size):
            if detect_collision(row_idx, col_idx, DIRECTIONS[current_dir_index], empty_spiral):
                empty_spiral[row_idx][col_idx] = 1
                last_move = True
            else:
                if DIRECTIONS[current_dir_index] == 'RIGHT':
                    col_idx -= 1
                elif DIRECTIONS[current_dir_index] == 'LEFT':
                    col_idx += 1
                elif DIRECTIONS[current_dir_index] == 'UP':
                    row_idx += 1
                elif DIRECTIONS[current_dir_index] == 'DOWN':
                    row_idx -= 1
                current_dir_index += 1 if current_dir_index+1<len(DIRECTIONS) else 0
                if not last_move:
                    return empty_spiral
                last_move = False
            if DIRECTIONS[current_dir_index] == 'RIGHT':
                col_idx += 1
            elif DIRECTIONS[current_dir_index] == 'LEFT':
                col_idx -= 1
            elif DIRECTIONS[current_dir_index] == 'UP':
                row_idx -= 1
            elif DIRECTIONS[current_dir_index] == 'DOWN':
                row_idx += 1
    return empty_spiral



print(spiralize(5))