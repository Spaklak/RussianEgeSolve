def f(x,y):
    if x > y or x  == 33: # тут 33 - это то число, которое нельзя
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x+1,y) + f(x*3,y) # тут +1 и *3 это действия 

print(f(19,21) * f(21,101)) # а тут траектория от 19 до 101, которая обязательно содержит 21