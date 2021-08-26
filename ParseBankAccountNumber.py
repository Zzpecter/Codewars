PARSE_DICT = {
    ' _ | ||_|': '0',
    '     |  |': '1',
    ' _  _||_ ': '2',
    ' _  _| _|': '3',
    '   |_|  |': '4',
    ' _ |_  _|': '5',
    ' _ |_ |_|': '6',
    ' _   |  |': '7',
    ' _ |_||_|': '8',
    ' _ |_| _|': '9'}
CHAR_LENGTH = 3


def split_list(input_list):
    return_list = []
    for i in range(0, len(input_list), CHAR_LENGTH):
        return_list.append(input_list[i:i + CHAR_LENGTH])
    return return_list


def parse_bank_account(bank_account):
    lines = bank_account.splitlines()
    chars = []
    for line in lines:
        if chars:
            new_chars = split_list(line)
            for index, new in enumerate(new_chars):
                chars[index] += new
        else:
            chars = split_list(line)

    output = ''
    for num in chars:
        output += PARSE_DICT.get(num, '0')

    return int(output)



# text = '    _  _     _  _  _  _  _ \n  | _| _||_||_ |_   ||_||_|\n  ||_  _|  | _||_|  ||_| _|\n'
text = ' _  _  _  _  _  _  _  _  _ \n| | _| _|| ||_ |_   ||_||_|\n|_||_  _||_| _||_|  ||_| _|\n'
print(parse_bank_account(text))
