#generate a binary number of len(distance_list) bits
#generate all binary numbers of that length
#pick the ones with num_towns activated bits

def count_ones(bin_str):
    count = 0
    for bit in bin_str:
        if bit == '1':
            count += 1
    return count


def get_combinations(distance_list, num_towns):
    combinations = []
    num_bits = len(distance_list)
    max_number = 0

    for i in range(num_bits):
        most_significant_bit_val = 2 ** i
        max_number += most_significant_bit_val

    for num in range(max_number+1):
        bin_num = bin(num)
        bin_str = str(bin_num)[2:]

        num_ones = count_ones(bin_str)
        if num_ones == num_towns:
            # format the string to have the same amount of bits
            while len(bin_str) < num_bits:
                bin_str = '0{}'.format(bin_str)
            combinations.append(bin_str)

    return combinations


def get_best_distance(distances, max_distance):
    current_max = 0
    for d in distances:
        if current_max < d <= max_distance:
            current_max = d
    if current_max == 0:
        current_max = None
    return current_max


def choose_best_sum(max_distance, num_towns, distance_list):
    combinations = get_combinations(distance_list, num_towns)
    distances = []
    for combi in combinations:
        distance = 0
        index = 0
        for char in combi:
            if char == '1':
                distance += distance_list[index]
            index += 1
        distances.append(distance)

    best_dist = get_best_distance(distances, max_distance)
    return best_dist
