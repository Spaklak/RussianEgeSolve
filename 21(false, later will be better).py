def f(x,s,p):
    if x + s >= 41 and (p == 2 or p == 4) :
        return True
    elif (x + s < 41 and p == 4) or x + s >= 41:
        return False
    if p % 2 == 1:
        return f(x+1,s+2,p+1) or f(x+2,s+1,p+1) or f(x,s*2,p+1) or f(x*2,s,p+1)
    else:
        return f(x+1,s+2,p+1) and f(x+2,s+1,p+1) and f(x,s*2,p+1) and f(x*2,s,p+1)

def f1(x,s,p):
    if x + s >= 41 and p == 2:
        return True
    else: 
        if x + s < 41 and p == 2:
            return False
        else:
            if x + s >= 41:
                return False
    if p % 2 == 1:
        return f1(x+1,s+2,p+1) or f1(x+2,s+1,p+1) or f1(x,s*2,p+1) or f1(x*2,s,p+1)
    else:
        return f1(x+1,s+2,p+1) and f1(x+2,s+1,p+1) and f1(x,s*2,p+1) and f1(x*2,s,p+1)

def f2(x,s,p):
    if x + s >= 41 and p == 4:
        return True
    else: 
        if x + s < 41 and p == 4:
            return False
        else:
            if x + s >= 41:
                return False
    if p % 2 == 1:
        return f2(x+1,s+2,p+1) or f2(x+2,s+1,p+1) or f2(x,s*2,p+1) or f2(x*2,s,p+1)
    else:
        return f2(x+1,s+2,p+1) and f2(x+2,s+1,p+1) and f2(x,s*2,p+1) and f2(x*2,s,p+1)

for i in range(1,32+1):
    if f(8,i,0):
        print(i)

print('=========')
for i in range(1,32+1):
    if f1(8,i,0):
        print(i)
print('=========')
for i in range(1,32+1):
    if f2(8,i,0):
        print(i)
print('=========')