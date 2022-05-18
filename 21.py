def f(x, s, p):
    if x + s >= 231 and (p == 4 or p == 2):
        return True
    elif (x + s < 231 and p == 4):
        return False
    elif x + s >= 231 and p < 4:
        return False 
    if p % 2 == 1:
        return f(x+1,s,p+1) or f(x*2,s,p+1) or f(x,s+1,p+1) or f(x,s*2,p+1)
    else:
        return f(x+1,s,p+1) and f(x*2,s,p+1) and f(x,s+1,p+1) and f(x,s*2,p+1)

for i in range(1,213+1):
    if f(i,17,0):
        print(i)

        