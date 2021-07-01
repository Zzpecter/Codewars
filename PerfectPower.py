def isPP(number):
    powers = list(range(2, 20))
    margin = 0.0002

    for power in powers:
        res = number ** (1 / power)
        res_int = int(round(res))
        if abs(res - res_int) <= margin:
            return [res_int, power]

print(isPP(216))