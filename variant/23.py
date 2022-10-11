def f(x,y,p):
    if x%2 ==0:
        p+=1
    if x>y or p>6:
        return 0
    if x==y and p==6:
        return 1

    return f(x+1,y,p) + f(x+3,y,p) + f(x+5,y,p)

print(f(3,25,0))