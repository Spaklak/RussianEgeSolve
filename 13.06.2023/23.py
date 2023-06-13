def f(x,y):
    if x >y:
        return 0
    if x == y:
        return 1
    return f(x+1,y) + f(x*2,y) + f(x*3,y)


count = 0
for i in range(2,15):
    if i % 2 == 0:
        if f(i,15) > 0:
            count += f(i,15)

print(count)