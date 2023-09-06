a = [2,3,5,7,11,13,17,19,23,29,31]
def f(x,y):
    if x > y or x in a:
        return 0
    if x == y:
        return 1
    return f(x+1,y)+f(x+2,y)+f(x*3,y)

print(f(8,16)*f(16,32))