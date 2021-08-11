REMOTE = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
          ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
          ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
          ['p', 'q', 'r', 's', 't', '.', '@', '0'],
          ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]


def get_indexes(letter):
    for index, row in enumerate(REMOTE):
        if letter in row:
            return index, row.index(letter)


def tv_remote(word):
    x_indexes = []
    y_indexes = []

    for letter in word:
        new_y, new_x = get_indexes(letter)
        x_indexes.append((new_x))
        y_indexes.append((new_y))

    current_x = 0
    current_y = 0
    moves = 0

    for _ in range(len(x_indexes)):
        new_x = x_indexes.pop(0)
        new_y = y_indexes.pop(0)

        moves_x = new_x - current_x
        moves_y = new_y - current_y

        moves += moves_x if moves_x >= 0 else moves_x * -1
        moves += moves_y if moves_y >= 0 else moves_y * -1

        current_y = new_y
        current_x = new_x
        moves += 1
    return moves


print(tv_remote("codewars"))
