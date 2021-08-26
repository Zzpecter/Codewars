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


def generate_output(grid):
    output = ''
    for row in grid:
        output += ''.join(letter for letter in row) + '\r\n'
    return output[:-2]


def interpreter(code, iterations, width, height):
    grid = [['0'] * width for _ in range(height)]
    grid_pos_x = grid_pos_y = 0

    if iterations == 0:
        return generate_output(grid)
    else:
        code_index = 0
        iteration = 0

        while True:
            worked = False
            increment_index = True
            instruction = code[code_index]

            if instruction == 'n':
                grid_pos_y = (grid_pos_y - 1) if grid_pos_y > 0 else height - 1
                worked = True
            elif instruction == 's':
                grid_pos_y = (grid_pos_y + 1) if grid_pos_y < height-1 else 0
                worked = True
            elif instruction == 'w':
                grid_pos_x = (grid_pos_x - 1) if grid_pos_x > 0 else width - 1
                worked = True
            elif instruction == 'e':
                grid_pos_x = (grid_pos_x + 1) if grid_pos_x < width-1 else 0
                worked = True
            elif instruction == '*':
                grid[grid_pos_y][grid_pos_x] = '1' if grid[grid_pos_y][grid_pos_x] == '0' else '0'
                worked = True
            elif instruction == '[':
                if grid[grid_pos_y][grid_pos_x] == '0':
                    code_index = find_closing_bracket(code, code_index + 1)
                    increment_index = False
                worked = True
            elif instruction == ']':
                if grid[grid_pos_y][grid_pos_x] != '0':
                    code_index = find_opening_bracket(code, code_index)
                    increment_index = False
                worked = True

            if worked:
                iteration += 1

            if increment_index:
                code_index += 1
            if code_index >= len(code) or iteration >= iterations:
                break

        return generate_output(grid)


print(interpreter("*[s[e]*]", 49, 5, 5))
