def f(x,y,p):
    if x + y >= 259 or p > 5:
        return p == 3 or p == 5
    if p % 2 == 0:
        return f(x+1,y,p+1) or f(x,y+1,p+1) or f(x*2,y,p+1) or f(x,y*2,p+1)
    else:
        return f(x+1,y,p+1) and f(x,y+1,p+1) and f(x*2,y,p+1) and f(x,y*2,p+1)

for i in range(1,242):
    if f(17,i,1):
        print(i)

# тут было и 19 и 20 и 21