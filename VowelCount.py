VOWELS = ['a', 'e', 'i', 'o', 'u']


def get_count(input_str):
    return len([letter for letter in input_str if letter in VOWELS])