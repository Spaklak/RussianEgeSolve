def f(x,c,m):
    if x >= 100: return c%2 == m%2
    if c == m: return 0

    h = [f(x+7,c+1,m),f(x*2,c+1,m)]

    return any(h) if (c+1)%2==m%2 else any(h)

for s in range(1,100):
    for m in range(1,5):
        if f(s,0,m):
            if m == 2: print(s,m)
            break