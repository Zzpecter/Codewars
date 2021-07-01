def pick_peaks(input_list):
    positions, peaks = [], []
    reference_min = input_list[0]
    reference_max = input_list[0]
    state = 'falling'  # rising or falling
    index = 0

    for value in input_list:
        if state == 'falling':
            if value <= reference_min:
                reference_min = value
            else:
                reference_max = value
                state = 'rising'
        elif state == 'rising':
            if value > reference_max:
                reference_max = value
            elif value == reference_max:
                pass
            else:
                state = 'falling'
                reference_min = value
                peaks.append(reference_max)
                positions.append(index-1)
        index += 1
    return {'pos': positions, 'peaks': peaks}

print(pick_peaks([2,1,3,1,2,2,2,2]))