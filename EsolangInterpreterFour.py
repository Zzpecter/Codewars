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


def generate_input(input):
    raw_input = ''
    for letter in input:
        raw_bits = format(ord(letter), 'b')
        while len(raw_bits) < 8:
            raw_bits = f'0{raw_bits}'
        raw_input += raw_bits[::-1]
    return list(raw_input)


def boolfuck(code, input=""):
    work_tape = []
    output_tape = []
    output_byte = ''
    input_tape = generate_input(input)
    pointer = 0
    code_index = 0

    while True:
        increment_index = True
        instruction = code[code_index]
        if instruction == '>':
            pointer += 1
            if pointer >= len(work_tape):
                work_tape.append('0')
        elif instruction == '<':
            pointer -= 1
            if pointer < 0:
                pointer = 0
                work_tape.insert(0, '0')
        elif instruction == '+':
            work_tape[pointer] = '0' if work_tape[pointer] == '1' else '1'
        elif instruction == '[':
            if work_tape[pointer] == '0':
                code_index = find_closing_bracket(code, code_index + 1)
                increment_index = False
        elif instruction == ']':
            if work_tape[pointer] != '0':
                code_index = find_opening_bracket(code, code_index)
                increment_index = False
        elif instruction == ',':
            work_tape.insert(code_index, input_tape.pop(0) if len(input_tape) > 0 else '0')
        elif instruction == ';':
            if pointer > len(work_tape):
                output_byte += work_tape[pointer]
            else:
                output_byte = output_byte + input_tape.pop(0) if len(input_tape) > 0 else '0'
            if len(output_byte) == 8:
                output_tape.append(chr(int(output_byte[::-1], 2)))
                output_byte = ''
            if code_index == len(code) - 2:
                # todo pad with zeros
                pass

        if increment_index:
            code_index += 1
        if code_index >= len(code):
            break
    return ''.join(output_tape)


print(boolfuck(";;;+;+;;+;+;+;+;+;+;;+;;+;;;+;;+;+;;+;;;+;;+;+;;+;+;;;;+;+;;+;;;+;;+;+;+;;;;;;;+;+;;+;;;+;+;;;+;+;;;;+;+;;+;;+;+;;+;;;+;;;+;;+;+;;+;;;+;+;;+;;+;+;+;;;;+;+;;;+;+;+;")  # "Codewars"
)