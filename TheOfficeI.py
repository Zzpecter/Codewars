def outed(meet, boss):
    total_support = 0
    for key, value in meet.items():
        if key == boss:
            total_support += 2*value
        else:
            total_support += value
    average_support = total_support / (len(meet))
    if average_support <= 5:
        return 'Get Out Now!'
    return 'Nice Work Champ!'
