
def tournament(n, fname):
    t = []
    for i in range(n):
        t.append([0]*n)
    # print(t)
    with open(fname) as f:
        for line in f:
                i,j,x,y = [int(x) for x in line.split()]
                i = i-1
                j = j-1
                t[i][j] = x - y
                t[j][i] = y - x
    return t

print(tournament(4,"example"))
