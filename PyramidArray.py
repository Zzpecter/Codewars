def pyramid(n):
    return [([1 for _ in range(i+1)]) for i in range(n)]


print(pyramid(9))
