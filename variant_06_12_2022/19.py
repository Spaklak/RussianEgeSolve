def f(x,y,p):
    if 107 <= x + y <= 170 or p > 3:
        return p == 4
    if x + y > 170:
        return p == 5
    else:
        if p%2 == 0:
            return f(x+10,y,p+1) or f(x*2,y,p+1) or f(x,y*2,p+1) or f(x,y+10,p+1)
        else:
            return f(x+10,y,p+1) and f(x*2,y,p+1) and f(x,y*2,p+1) and f(x,y+10,p+1)
for s in range(1,101):
    if f(5,s,1):
        print(s)