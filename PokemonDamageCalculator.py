TYPE_DICT = {0: 'fire', 1: 'water', 2: 'grass', 3: 'electric'}
EFFECTIVENESS_MATRIX = [[0.5, 0.5, 2.0, 1.0],
                        [2.0, 0.5, 0.5, 0.5],
                        [0.5, 2.0, 0.5, 1.0],
                        [1.0, 2.0, 1.0, 0.5]]

def get_efectiveness_ratio(first_type, second_type):
    index_one, index_two, effectiveness_ratio = None, None, None
    for k, v in TYPE_DICT.items():
        if v == first_type:
            index_one = k
        if v == second_type:
            index_two = k

    if index_one is not None and index_two is not None:
        effectiveness_ratio = EFFECTIVENESS_MATRIX[index_one][index_two]
    return effectiveness_ratio


def calculate_damage(your_type, opponent_type, attack, defense):
    effectiveness_ratio=get_efectiveness_ratio(your_type.lower(), opponent_type.lower())
    damage = 0
    if effectiveness_ratio is not None:
        damage = 50 * (attack/defense) * effectiveness_ratio
    return damage
