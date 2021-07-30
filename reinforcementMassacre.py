def place_bombs(fight_list, airstrike):
    for index, tile in enumerate(airstrike):
        if tile == '*':
            fight_list[index] = '*'
    return fight_list


def detonate(fight_list):
    bomb = False

    for index, tile in enumerate(fight_list):
        if tile == '*' and not bomb:
            bomb = True
        elif tile != '*' and bomb:
            fight_list[index] = '_'
            bomb = False

    for index, tile in enumerate(fight_list.__reversed__()):
        if tile == '*' and not bomb:
            bomb = True
        elif tile != '*' and bomb:
            fight_list[-index-1] = '_'
            bomb = False
    return fight_list


def create_reinforcements_list(reinforces):
    battlefield = reinforces.pop(0)
    reinforcement_list = [[] for _ in range(len(battlefield))]
    for battalion in reinforces:
        for index, soldier in enumerate(battalion):
            reinforcement_list[index].append(soldier)
    return list(battlefield), reinforcement_list


def reinforce(battlefield, reinforcements):
    for index, tile in enumerate(battlefield):
        if tile == '_' or tile == '*':
            if reinforcements[index]:
                battlefield[index] = reinforcements[index].pop(0)
            else:
                battlefield[index] = '_'
    return battlefield, reinforcements


def alphabet_war(reinforces, airstrikes):
    battlefield, reinforcements = create_reinforcements_list(reinforces)
    for index, airstrike in enumerate(airstrikes):
        battlefield = detonate(place_bombs(battlefield, airstrike))
        battlefield, reinforcements = reinforce(battlefield, reinforcements)
    return ''.join(battlefield)

reinforces=["g964xxxxxxxx",
            "myjinxin2015",
            "steffenvogel",
            "smile67xxxxx",
            "giacomosorbi",
            "freywarxxxxx",
            "bkaesxxxxxxx",
            "vadimbxxxxxx",
            "zozofouchtra",
            "colbydauphxx" ]
airstrikes=["* *** ** ***",
            " ** * * * **",
            " * *** * ***",
            " **  * * ** ",
            "* ** *   ***",
            "***   ",
            "**",
            "*",
            "*" ]
print(alphabet_war(reinforces, airstrikes))