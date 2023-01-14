def f(x,y,c):
    if x == y and c == 7:
        return 1
    if x > y or c > 7:
        return 0
    return f(x+1,y,c+1) + f(x+4,y,c+1) + f(x * 2,y,c+1)

print(f(3,27,0))