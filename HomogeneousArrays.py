def filter_homogenous(arrays):
    output=[]
    for array in arrays:
        type_array = [type(item) for item in array]
        if len(set(type_array)) <= 1 and len(array) > 0:
            output.append(array)
    return output

print(filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]))