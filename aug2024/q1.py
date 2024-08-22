def advance(t):
    (h,m) = t
    m = m + 10
    if m > 60:
        h=h+1
        m=m-60
    return (h,m)
