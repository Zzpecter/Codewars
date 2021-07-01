def decimal_to_hex(decimal_number):
    hex_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    counter = 0
    remainder = []
    answer = ""
    if decimal_number > 255:
        answer = "FF"
    elif decimal_number > 0:
        while decimal_number > 0:
            remainder.append(decimal_number % 16)
            decimal_number = decimal_number // 16
            counter = counter + 1
        for reverse in remainder[::-1]:
            answer = answer + hex_list[reverse]
    else:
        answer = "00"
    return answer if len(answer) == 2 else f'0{answer}'


def rgb(r, g, b):
    return(f"{decimal_to_hex(r)}{decimal_to_hex(g)}{decimal_to_hex(b)}")
