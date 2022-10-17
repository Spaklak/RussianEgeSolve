def f(x,y,p):
    if x + y >= 88 or p > 3:
        return p == 3
    return f(x+1, y, p +1) or f(x * 3,y,p+1) or f(x,y+1,p+1) or f(x,y*3,p+1)

for i in range(1,82):
    if f(6,i,1):
        print(i)
        break