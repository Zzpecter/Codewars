def get_current_rail(num_rails, current_rail, rising):
    if rising:
        if current_rail == num_rails:
            rising = False
            current_rail -= 1
        else:
            current_rail += 1
    else:
        if current_rail == 0:
            rising = True
            current_rail += 1
        else:
            current_rail -= 1
    return current_rail, rising


def read_rail_by_rail(rails):
    encoded_result = ''
    for rail in rails:
        encoded_result += "".join(rail)
    return encoded_result


def encode_rail_fence_cipher(input_text, n_rails):
    rails = [[] for _ in range(n_rails)]
    current_rail = 0
    rising = True
    for letter in input_text:
        for rail_idx in range(len(rails)):
            if current_rail == rail_idx:
                rails[rail_idx].append(letter)
        current_rail, rising = get_current_rail(len(rails)-1, current_rail, rising)
    return read_rail_by_rail(rails)


def decode_rail_fence_cipher(input_text, n_rails):
    rails = [[] for _ in range(n_rails)]

    current_rail = 0
    rising = True
    rail_positions = []
    for _ in input_text:
        for rail_idx in range(len(rails)):
            if current_rail == rail_idx:
                rail_positions.append(rail_idx)
        current_rail, rising = get_current_rail(len(rails) - 1, current_rail, rising)

    for rail_idx in range(len(rails)):
        range_to_cut = rail_positions.count(rail_idx)
        rails[rail_idx].append(list(input_text[:range_to_cut]))
        input_text = input_text[range_to_cut:]

    rail_indexes = [0]*len(rails)
    result = ''

    for position in rail_positions:
        current_rail = rails[position]
        current_position = rail_indexes[position]
        result += current_rail[0][current_position]
        rail_indexes[position] += 1

    return result

