def f(x,y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x-2,y) + f(x//2,y)

print(f(28,10) * f(10,1))