def f(a,c,m):
    if a >= 55: return c%2 == m%2
    if c == m: return 0

    h = ([f(a+1,c+1,m), f(a+4,c+1,m), f(a*3,c+1,m)])

    return any(h) if (c+1)%2==m%2 else all(h)

for s in range(1,55):
    for m in range(1,5):
        if f(s,0,m):
            if m == 4: print(s,m)
            break