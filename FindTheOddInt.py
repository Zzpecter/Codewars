from collections import Counter
def find_it(seq):
    occurrence_dict = Counter(seq)
    for key, value in occurrence_dict.items():
        if value%2 != 0:
            return key
