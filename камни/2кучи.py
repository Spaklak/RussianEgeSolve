def f(a,b,c,m):
    if a + b >= 74: return c%2 == m%2
    if c == m: return 0

    h = [f(a+2,b,c+1,m), f(a*2,b,c+1,m), f(a,b+2,c+1,m), f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2 == m % 2 else all(h) # если неудачый ход Пети, то мы all меняем на any

for s in range(1,67):
    for m in range(1,5):
        if f(7,s,0,m)==1:
            if m == 4: print(s,m)
            break