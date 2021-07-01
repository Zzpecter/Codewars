def solution(text):
    spaced_string =''
    for letter in text:
        spaced_string += letter if letter.islower() else f' {letter}'
    return spaced_string
