def f(x, s, p):
    if x + s >= 67 and p == 3:
        return True
    elif (x+s<67 and p == 3) or x+s>=67:
        return False
    if p % 2 == 0:
        return f(x+1, s, p+1) or f(x, s+1, p+1) or f(x+s, s, p+1) or f(x, s+x, p+1)
    else:
        return f(x+1, s, p+1) and f(x, s+1, p+1) and f(x+s, s, p+1) and f(x, s+x, p+1)

for i in range(1, 67):
    if f(9,i,0):
        print(i)