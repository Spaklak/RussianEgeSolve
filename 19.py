def f(x, s, p):
    if x + s >= 67 and p == 2:
        return True
    elif x+s<67 and p == 2:
        return False
    return f(x+1, s, p+1) or f(x, s+1, p+1) or f(x+s, s, p+1) or f(x, s+x, p+1)

for i in range(1, 57+1):
    if f(9,i,0):
        print(i)
        break