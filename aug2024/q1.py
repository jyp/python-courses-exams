# assumption: a timestamp can refer to different days and thus hours may be >24.

def advance(t):
    (h,m) = t
    m = m + 10
    if m > 60:
        h=h+1
        m=m-60
    return (h,m)
