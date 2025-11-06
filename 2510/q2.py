# task 2a
def find_subsequence(sub, seq):
    return list(find_subsequence_gen(sub, seq))

# task 2b
def take_n(n, gen):
    i = 0
    vals = []
    for val in gen:
        i += 1
        if i > n:
            break
        vals.append(val)
    return vals

# task 2c
def find_subsequence_gen(sub, gen):
    l = ""
    pos = 0
    for m in gen:
        l = (l+m)[-len(sub):]
        if l == sub:
            yield pos-len(sub)+1
        pos += 1

#### other acceptable answer for 2a:
def find_subsequence(sub, seq):
    poss = []
    for m in range(len(seq)):
        if seq[m:m+len(sub)] == sub:
            poss.append(m)
    return poss

