def f(x,y):
    if x == y:
        return 1
    if x > y or x == 60:
        return 0
    if x < y:
        return f(x+5,y) + f(x*5,y)

print(f(5,30) * f(30,280))