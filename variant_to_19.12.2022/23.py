def f(x,y,p):
    if x > y:
        return 0
    if x == y and p == 8:
        return 1
    if x < y and p < 8:
        return f(x+2,y,p+1) + f(x+4,y,p+1) + f(x*2,y,p+1)
    else:
        return 0
print(f(4,64,0))
