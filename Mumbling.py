def accum(s):
    accumulator = 1
    words = []
    for character in s:
        words.append("".join([character]*accumulator).capitalize())
        accumulator += 1
    return '-'.join(words)
