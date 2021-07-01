def sum_of_intervals(intervals):
    numbers = []
    for entry in intervals:
        for number in range(entry[0],entry[1]):
            numbers.append(number)
    return len(set(numbers))
