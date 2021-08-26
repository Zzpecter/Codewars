def find_closing_bracket(search_list, start_index):
    bracket_count = 0
    for index, element in enumerate(search_list[start_index:]):
        if bracket_count == 0 and element == ']':
            return index + start_index + 1
        elif element == '[':
            bracket_count += 1
        elif bracket_count > 0 and element == ']':
            bracket_count -= 1
    return None


def find_opening_bracket(search_list, start_index):
    bracket_count = 0
    for index, element in enumerate(reversed(search_list[:start_index])):
        if bracket_count == 0 and element == '[':
            return start_index - index
        elif element == ']':
            bracket_count += 1
        elif bracket_count > 0 and element == '[':
            bracket_count -= 1
    return None

def interpreter(code, tape):
    work_tape = list(tape)
    pointer = 0
    code_index = 0

    while True:
        increment_index = True
        instruction = code[code_index]
        if instruction == '>':
            pointer += 1
        elif instruction == '<':
            pointer -= 1
        elif instruction == '*':
            work_tape[pointer] = '0' if work_tape[pointer] == '1' else '1'
        elif instruction == '[':
            if work_tape[pointer] == '0':
                code_index = find_closing_bracket(code, code_index + 1)
                increment_index = False
        elif instruction == ']':
            if work_tape[pointer] != '0':
                code_index = find_opening_bracket(code, code_index)
                increment_index = False
        if increment_index:
            code_index += 1
        if code_index >= len(code) or pointer >= len(work_tape) or pointer < 0:
            break
    return ''.join(work_tape)

print(interpreter("*", "00101100") ) # "10101100"