def solution(string,markers):
    string_list = string.split("\n")
    new_list = []

    for item in string_list:
        aux_string = ""
        for char in item:
            if char in markers:
                break
            else:
                aux_string += char
        new_list.append(aux_string.strip())
    return "\n".join(new_list)
