'''
1000
300

100000
25000
'''
minim = 100000000000000000000000000000000
data = open('27B.txt')
data = [int(x) for x in data.read().split()]
for i in range(len(data)):
    for x in range(i+25000, len(data)):
        if (data[i] * data[x]) % 157 == 0:
            minim = min(data[i]*data[x], minim)

print(minim)