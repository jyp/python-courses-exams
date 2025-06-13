def parse(base, notation):
    l = []
    for c in notation:
        if c in base:
            l.append(base[c])
        else:
            return None
    return l

def powers(m, n):
    pows = []
    for i in range(n):
        pows.append(m**i)
    pows.reverse()
    return pows


def n_ary(base, notation):
    digits = parse(base, notation)
    if not digits:
        return None
    else:
        pows = powers(len(base), len(digits))
        print(pows)
        result = 0
        for i in range(len(digits)):
            result += digits[i] * pows[i]
        return result


decimal = dict((str(i), i) for i in range(10))
nonary = dict((str(i), i) for i in range(9))
hexadecimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}