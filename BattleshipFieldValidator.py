

def get_diagonals(field):
    height, width = len(field), len(field[0])
    nemo_transform = [[field[height-1-q][p-q] for q in range(min(p, height-1), max(0, p-width+1)-1, -1)] for p in range(height+width-1)]
    return check_nemo(nemo_transform)


def get_anti_diagonals(field):
    height, width = len(field), len(field[0])
    nemo_transform = [[field[p - q][q] for q in range(max(p - height + 1, 0), min(p + 1, width))] for p in range(height + width - 1)]
    return check_nemo(nemo_transform)


def check_nemo(nemo):
    for diagonal in nemo:
        is_one = False
        for number in diagonal:
            if number == 1 and not is_one:
                is_one = True
            elif number == 1 and is_one:
                return False
            else:
                is_one = False
    return True

def check_if_sub(field, row, column, check="up-down"):
    sub = True
    if check == "up-down":
        if row > 0 and field[row - 1][column] == 1:
            sub = False
        elif row < (len(field) - 1) and field[row + 1][column] == 1:
            sub = False
    else:
        if column > 0 and field[row][column-1] == 1:
            sub = False
        elif column < (len(field) - 1) and field[row][column+1] == 1:
            sub = False
    return sub


def update_ships(ships, key):
    ships_available = ships[key]
    ships.update({key: ships_available - 1})


def validate_battlefield(field):
    ships = {
        1: 4,  # 4 subs
        2: 3,  # 3 cruisers
        3: 2,  # 2 destroyers
        4: 1  # 1 battleship
    }
    #check diags first:
    if not get_diagonals(field) or not get_anti_diagonals(field):
        return False

    #if sub is on last column it does not get verified
    #horizontal pass
    for row in range(len(field)):
        current_length = 0
        for column in range(len(field[0])):
            if column == 1 and row == 9:
                pass
            if field[row][column] == 1:
                found_col = column
                current_length += 1

            else:
                if current_length > 1: #ignore subs
                    # substract the ship from the dict
                    ships_available = ships.get(current_length, None)
                    if ships_available is None:
                        return False
                    ships.update({current_length: (ships_available - 1)})
                elif current_length == 1: #check adjacent fields to see if sub
                    sub = check_if_sub(field, row, found_col)
                    if sub:
                        update_ships(ships, current_length)
                current_length = 0
            if column == len(field) - 1 and field[row][column] == 1: #lst column, verify before passing row
                if current_length > 1: #ignore subs
                    # substract the ship from the dict
                    ships_available = ships.get(current_length, None)
                    if ships_available is None:
                        return False
                    ships.update({current_length: (ships_available - 1)})
                elif current_length == 1: #check adjacent fields to see if sub
                    sub = check_if_sub(field, row, found_col)
                    if sub:
                        update_ships(ships, current_length)

    #vertical pass
    for column in range(len(field[0])):
        current_length = 0
        for row in range(len(field)):
            if field[row][column] == 1:
                current_length += 1
            else:
                if current_length > 1: #ignore subs
                    # substract the ship from the dict
                    ships_available = ships.get(current_length, None)
                    if ships_available is None:
                        return False
                    ships.update({current_length: ships_available - 1})
                current_length = 0

        if row == len(field) - 1 and field[row][column] == 1:  # lst row, verify before passing
            if current_length > 1:  # ignore subs
                # substract the ship from the dict
                ships_available = ships.get(current_length, None)
                if ships_available is None:
                    return False
                ships.update({current_length: (ships_available - 1)})

    all_ships_placed = True
    for key, value in ships.items():
        if value != 0:
            all_ships_placed = False
            break
    print(ships)
    return all_ships_placed


battleField = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(battleField))
