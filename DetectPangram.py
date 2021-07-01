import string

def is_pangram(input_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pure_letters = ''
    for char in input_text:
        if char.isalpha():
            pure_letters += char.lower()
    return False if set(alphabet) != set(pure_letters) else True
