def f(x,y,c,m):
    if x + y == 13: return c % 2 == m % 2 
    if c == m: return 0

    h = [f(x+1,y,c+1,m), f(x+2,y,c+1,m), f(x,y+1,c+1,m), f(x,y+2,c+1,m)]

    return any(h) if (c+1) % 2 == m % 2 else all(h)

for s in range(1,10):
    for m in range(1,5):
        if f(3,s,0,m):
            if m == 4: print(s,m)
            break

# 19 - idk
# 20 - 5,6
# 21 - 4
