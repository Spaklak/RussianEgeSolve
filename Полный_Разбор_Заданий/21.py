'''
Далее будем рассматривать отличия от 20й
'''
def f(x,y,p):
    if x + y >= 88 or p > 5: # заменили на 5
        return p == 3 or p == 5 # добавили условие для p == 3 и p == 5
    if p % 2 == 0: # поменяли знак с != на ==
        return f(x+1, y, p +1) or f(x * 3,y,p+1) or f(x,y+1,p+1) or f(x,y*3,p+1)
    else:
        return f(x+1, y, p +1) and f(x * 3,y,p+1) and f(x,y+1,p+1) and f(x,y*3,p+1)

for i in range(1,82):
    if f(6,i,1):
        print(i)
'''
Дальше всё также
'''