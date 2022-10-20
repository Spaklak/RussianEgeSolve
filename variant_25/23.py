spisok = []
count = 0
def f(x,y):
    global count
    global spisok
    if x > y:
        return 0
    if x == y:
        return 1
    if x % 2 != 0 and x not in spisok:
        count += 1
        spisok.append(x)
    if x < y:
        return f(x+3,y) + f(x*3,y)

f(1,99)
print(count)