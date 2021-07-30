

def detonate(battlefield, bomb_index, increment=1, shelter_start='[', shelter_end=']'):
    kill = True
    exploding = True
    while exploding:
        current_tile = battlefield[bomb_index]
        if current_tile == shelter_start:
            kill = False
            battlefield[bomb_index] = '_'
        elif kill:
            battlefield[bomb_index] = '_'
        elif current_tile == shelter_end:
            battlefield[bomb_index] = '_'
            exploding = False
        if bomb_index < 0 or bomb_index >= len(battlefield):
            exploding = False
        bomb_index += increment
    return battlefield


def alphabet_war(battlefield):
    battlefield = list(battlefield)
    if '#' in battlefield:
        for index, tile in enumerate(battlefield):
            if tile == '#':
                battlefield = detonate(battlefield, index)
                battlefield = detonate(battlefield, index, -1, shelter_start=']', shelter_end='[')
    return ''.join(battlefield).replace('_', '')

print(alphabet_war('[a]#[b]#[c]'))
