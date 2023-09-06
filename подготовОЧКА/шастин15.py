def f(a,x,y):
    return (x >= 11) or ((3 * x) < y) or ((x * y) < a)

for a in range(10000):
    if all(f(a,x,y) for x in range(10000) for y in range(10000)):
        print(a)
        break