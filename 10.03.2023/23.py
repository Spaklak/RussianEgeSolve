import sys

sys.setrecursionlimit(2000)

def f(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    if (str(x)[-1] == '1' or str(x)[-1] == '0') and x < y:
        return f(x+1,y) + f(x+10,y)
    if x < y:
        r = int(str(x)[-1])
        return f(x+1,y) + f(x+10,y) + f(x*r,y)


print(f(10,220))