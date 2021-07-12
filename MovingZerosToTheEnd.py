def move_zeros(array):
    zero_array = []
    while 0 in array:
        array.remove(0)
        zero_array.append(0)
    return array+zero_array
