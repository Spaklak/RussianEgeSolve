def f(x,y):
    if x > y or x == 17:
        return 0
    if x == y: 
        return 1
    if x < y:
        return f(x+1,y) + f(x*2,y) + f(x**2,y)
    
print(f(2,16)*f(16,65))