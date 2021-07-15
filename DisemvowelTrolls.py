VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def disemvowel(message):
    return ''.join(letter if letter not in VOWELS else '' for letter in message)
