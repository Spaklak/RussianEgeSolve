def f(x,y):
    if y == 5:
        a.append(x)
    else:
        f(x+2,y+1)
        f(x+3,y+1) 
        f(x * 2, y+1) 



a = []  
f(10,0)
print(len(set(a)))