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


def brain_luck(code, program_input):

    tape = [0]
    tape_pointer = 0
    output = ''
    code_index = 0
    finished = False
    input_list = [ord(letter) for letter in program_input]

    while not finished:
        increment_index = True
        instruction = code[code_index]
        if instruction == '>':
            tape_pointer += 1
            if tape_pointer >= len(tape):
                tape.append(0)
        elif instruction == '<':
            tape_pointer -= 1
            if tape_pointer < 0:
                tape_pointer = 0
                tape.insert(0, 0)
        elif instruction == '+':
            tape[tape_pointer] = (tape[tape_pointer] + 1) if tape[tape_pointer] < 255 else 0
        elif instruction == '-':
            tape[tape_pointer] = (tape[tape_pointer] - 1) if tape[tape_pointer] > 0 else 255
        elif instruction == '.':
            output += chr(tape[tape_pointer])
        elif instruction == ',':
            tape[tape_pointer] = input_list.pop(0)
        elif instruction == '[':
            if tape[tape_pointer] == 0:
                code_index = find_closing_bracket(code, code_index+1)
                increment_index = False
        elif instruction == ']':
            if tape[tape_pointer] != 0:
                code_index = find_opening_bracket(code, code_index)
                increment_index = False
        if increment_index:
            code_index += 1
        if len(input_list) == 0 and code_index >= len(code):
            finished = True

    return output

print(ord(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9))))
