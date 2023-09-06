'''
import math

number=int(input())

for i in range(2, int(math.sqrt(number)) + 1): # обычно делитель не будет больше корня
    while (number % i == 0): # while, а не if
        print(i)
        number //= i # убираем множитель из числа

'''

'''
data = open('27A.txt').read()
countMain = 0
data = [int(x) for x in data.split()]
for i1 in range(len(data)):
    for i2 in range(i1+1,len(data)):
        if (data[i1] + data[i2]) % 1111 == 0:
            proizv = data[i1] * data[i2]
            count = 0
            for i in range(2, int(proizv**0.5) + 1):
                while proizv % i == 0:
                    count +=1
                    proizv//=i
                if count >= 10:
                    break
            if count >= 10:
                countMain += 1

print(countMain)
'''

def f(n):
    count = 0
    for i in range(2,n):
        while n % i == 0:
            count += 1
            n //= i
    
    return count

data = open('27A.txt').read()
data = [int(x) for x in data.split()]
prostie = []
for i in data:
    prostie.append([f(i),i])

prostie.sort()

count = 0
for i in range(len(prostie)):
    for x in range(i+1, len(prostie)):
        if prostie[i][0] + prostie[x][0] >= 10:
            if (prostie[i][1] + prostie[x][1]) % 1111 == 0:
                count += 1

print(count)