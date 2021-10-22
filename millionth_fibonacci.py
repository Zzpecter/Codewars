def fibonacci(n):
    def fib_inner(n):
        if n == 0:
            return 0, 2
        u, v = fib_inner(n >> 1)
        q = (n & 2) - 1
        u, v = u * v, v * v + 2*q
        if n & 1:
            u1 = (u + v) >> 1
            return u1, 2*u + u1
        return u, v

    u, v = fib_inner(n >> 1)
    if n & 1:
        q = (n & 2) - 1
        u1 = (u + v) >> 1
        return v * u1 + q
    return u * v


def fib(n):
    positive = True
    pair = True if n % 2 == 0 else False
    if n < 0:
        n *= -1
        positive = False
    if not positive and pair:
        print(fibonacci(n) * -1)
    else:
        print(fibonacci(n))


if __name__ == '__main__':
    n = int(input())
    fib(n)