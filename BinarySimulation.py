def inverse_bits(binary, start, end):
    for index, digit in enumerate(binary):
        if index in range(start, end+1):
            binary[index] = '0' if digit == '1' else '1'
    return binary

def binary_simulation(binary, instruction_list):
    query_results = []
    binary = list(binary)
    for instruction in instruction_list:
        if instruction[0] == 'I':
            binary = inverse_bits(binary, instruction[1]-1, instruction[2]-1)
        else:
            query_results.append(binary[instruction[1]-1])
    return query_results

print(binary_simulation("0011001100", [['I', 1, 10], ['I', 2, 7], ['Q', 2], ['Q', 1], ['Q', 7], ['Q', 5]]))
#[ '0', '1', '1', '0' ]