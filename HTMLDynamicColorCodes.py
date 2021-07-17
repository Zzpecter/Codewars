import random
language = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def generate_color_rgb():
    return ''.join(language[random.randint(0, 15)] for _ in range(6))
