def f(x,y):
    if x % 2 == 0 and x < 100:
        a.append(x)
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 3, y) + f(x * 3, y)

a = []

f(3,100)

print(len(set(a)))