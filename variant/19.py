def f(x,z,p):
    if z < 0:
        return False
    elif (x >= 51 or p > 3) and z > 0:
        return p == 3
    return f(x+1,z-1,p+1) or f(x+2,z-2,p+1) or f(x*2,z-x*2,p+1)

for i in range(1,51):
    if f(i,60,1):
        print(i)

#неверно