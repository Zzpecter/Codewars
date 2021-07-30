LEFT_FIGHTERS = {'w': 4, 'p': 3, 'b': 2, 's': 1}
RIGHT_FIGHTERS = {'m': 4, 'q': 3, 'd': 2, 'z': 1}


def bomb_da_field(fight_list):
    bomb = False

    for index, tile in enumerate(fight_list):
        if tile == '*' and not bomb:
            bomb = True
        elif tile != '*' and bomb:
            fight_list[index] = '_'
            bomb = False

    for index, tile in enumerate(fight_list.__reversed__()):
        if tile == '*' and not bomb:
            bomb = True
        elif tile != '*' and bomb:
            fight_list[-index-1] = '_'
            bomb = False
    return ''.join(fight_list).replace('_', '')

def alphabet_war(fight):
    fight = bomb_da_field(list(fight))

    force_left = sum(LEFT_FIGHTERS[fighter] for fighter in fight if fighter in LEFT_FIGHTERS.keys())
    force_right = sum(RIGHT_FIGHTERS[fighter] for fighter in fight if fighter in RIGHT_FIGHTERS.keys())

    if force_left == force_right:
        return "Let's fight again!"
    return 'Left side wins!' if force_left > force_right else 'Right side wins!'

print(alphabet_war("*eqq*qq*mz**bbb*ddpmcb***"))