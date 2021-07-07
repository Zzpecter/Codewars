import numpy as np
from numpy import inf


def get_force_by_row(row, column):
    return 1 / (row * np.arange(2, column+2) ** (2 * row))


def doubles(row, column):
    '''Calculates the force of a box of magnets. See Magnet particules in boxes
    for more details'''
    total_force = 0
    for current_row in range(1, row+1):
        row_force = get_force_by_row(current_row, column)
        row_force[row_force == inf] = 0
        total_force += np.sum(row_force)
    return total_force

# Timed out one-liner solution:
# def get_force_by_cell(row, column):
#     return 1 / (row * ((column + 1) ** (2 * row)))
#
# def doubles(max_row, max_col):
#     return sum([get_force_by_cell(row+1, column+1) for row in range(max_row) for column in range(max_col)])

print(doubles(20, 10000))