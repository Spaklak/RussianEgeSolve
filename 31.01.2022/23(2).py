def f(x,y,c):
    global a
    if x == y:
        a.append(c)
        return 1
    if x > y or c >= 18:
        return 0
    if x < y:
        return f(x+1,y,c+1) + f(x*2,y,c+1) + f(x * 3,y,c+1)

a = []
f(1,32718,0)
print(min(a))