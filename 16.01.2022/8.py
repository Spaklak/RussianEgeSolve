count = 0
for i in range(100,1000):
    i = str(i)
    if i[0] <= i[1] and i[1] <= i[2]:
        count +=1
print(count)