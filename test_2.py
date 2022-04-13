from collections import Counter


def find_it(seq):
    return [list(dict(Counter(seq)).items())[i][0] for i in range(len(list(dict(Counter(seq)).items()))) if
            list(dict(Counter(seq)).items())[i][1] % 2 == 1][0]


a = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
assert find_it(a) == 5
