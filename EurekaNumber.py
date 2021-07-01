#link: https://www.codewars.com/kata/5626b561280a42ecc50000d1
def is_eureka_number(number):
    power=1
    sum_number=0
    for character in str(number):
        sum_number += int(character) ** power
        power +=1
    return True if sum_number == number else False

def sum_dig_pow(a, b): 
    numbers = []

    for number in range(a,b+1):
        if is_eureka_number(number):
            numbers.append(number)
    
    return numbers
        
