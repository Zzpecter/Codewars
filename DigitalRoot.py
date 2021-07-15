def digital_root(n):
    sum_of_digits = sum(int(digit) for digit in str(n))
    if sum_of_digits > 9:
        return digital_root(sum_of_digits)
    return sum_of_digits
