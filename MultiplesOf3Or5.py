def solution(number):
    total =0
    return sum(total + num if (num%3 == 0 or num%5==0) else total for num in range(number))
