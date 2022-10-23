def f(x,p):
    if x >= 165 or p > 3:
        return p == 2
    return f(x+1,p+1) or f(x+4,p+1) or f(x*2,p+1)

for i in range(1,165):
    if f(i,1):
        print(i)
        # ПОДУМАТЬ