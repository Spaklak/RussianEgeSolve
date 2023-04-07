def f(a,c,m):
    if a >= 22: return c % 2 == m % 2
    if c == m: return 0

    if a % 2 == 0:
        h = [f(a+1,c+1,m), f(a+2,c+1,m)]
    else:
        h = [f(a+1,c+1,m), f(a+2,c+1,m), f(a*2,c+1,m)]
    return any(h) if (c+1) % 2 == m % 2 else all(h)

for s in range(1,22):
    for m in range(1,10):
        if f(s,0,m):
            if m == 5: print(s,m)
            break