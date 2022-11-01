import sys
import math
sys.setrecursionlimit(2000)
count = 0
a = []
def f(x,y):
    global count
    global a
    if x > y or x == 6:
        return 0
    if x == y:
        return 1
    if x < y:
        if count == 0:
            return f(x+3,y) + f(x**2,y) + f(x+1,y)
        else:
            if x - a[count] == 1:
                a.append(x)
                count+=1
                return f(x+3,y) + f(x**2,y)
            elif math.sqrt(x) == a[count]:
                a.append(x)
                count+=1
                return f(x+1,y) + f(x+3,y)
            elif x - a[count] == 3:
                a.append(x)
                count+=1
                return f(x+1,y) + f(x**2,y)

print(f(1,5) * f(5,25))