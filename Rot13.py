ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def get_rot13(letter):
    index = ALPHABET.index(letter.upper()) + 13
    if index >= len(ALPHABET):
        index %= len(ALPHABET) 
    return ALPHABET[index].lower() if letter.islower() else ALPHABET[index]

def rot13(message):
    return_string =''
    for letter in message:
        return_string += get_rot13(letter) if letter.upper() in ALPHABET else letter
    return return_string
