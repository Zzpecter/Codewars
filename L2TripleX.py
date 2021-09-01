def triple_x(s):
    for index, letter in enumerate(s):
        if letter == 'x':
            try:
                return True if s[index+1] == 'x' and s[index+2] == 'x' else False
            except:
                return False
    return False

print(triple_x_two("softXxxx kitty, warm kitty, xxxxx"))