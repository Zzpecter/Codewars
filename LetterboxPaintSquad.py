def paint_letterboxes(start, finish):
    counts = [0] * 10
    for number in range(start, finish + 1):
        for digit in str(number):
            counts[int(digit)] += 1
    return counts
