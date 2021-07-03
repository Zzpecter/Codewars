LOVE_LANGUAGES = ["words", 'acts', 'gifts', 'time', 'touch']


def love_language(partner, weeks):
    love_score = {
        "words": 0,
        "acts": 0,
        "gifts": 0,
        "time": 0,
        "touch": 0
    }
    iteration_list = []
    while len(iteration_list) < weeks * 7:
        iteration_list.extend(LOVE_LANGUAGES)
    iteration_list = iteration_list[:weeks * 7]

    for language in iteration_list:
        response = partner.response(language)
        if response == 'positive':
            update_value = love_score[language] + 1
            love_score[language] = update_value
    print(love_score)

    return max(love_score, key=love_score.get)
love_language("AS", 6)
