def f(x,y,z):
    if x > y or z > 3:
        return 0
    elif x == y and z <= 3:
        return 1
    elif x < y:
        return f(x+2,y,z) + f(x*3,y,z+1) + f(x*5,y,z+1)

print(f(2,200,0))