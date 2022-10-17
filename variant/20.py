def f(x,y,p):
    if x + y >= 88 or p > 4:
        return p == 4
    if p % 2 != 0:
        return f(x+1, y, p +1) or f(x * 3,y,p+1) or f(x,y+1,p+1) or f(x,y*3,p+1)
    else:
        return f(x+1, y, p +1) and f(x * 3,y,p+1) and f(x,y+1,p+1) and f(x,y*3,p+1)

for i in range(1,82):
    if f(6,i,1):
        print(i)