def f(x,p):
    if 50 <= x <= 119 or p > 4:
        return p == 4
    if x > 119:
        return p == 5
    else:
        if p%2 == 0:
            return f(x+2,p+1) and f(x*3,p+1)
        else:
            return f(x+2,p+1) or f(x*3,p+1)
count = 0
for i in range(1,50):
    if f(i,1):
        print(i)