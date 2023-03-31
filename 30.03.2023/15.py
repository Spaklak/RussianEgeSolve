p = [1,2,3,4,5,6,7,8,9,10]
q = [2,4,8,10]
a = [2,4,8,10]
for i in range(1,11):
    l = True
    for x in range(1,1000):
        l = ((x in q) <= (x in a)) and ((x in a) <= (x in p))
        if l == False:
            a.pop()
            break

print(a)