data = open('17.txt')

data = [int(x) for x in data.read().split()]
a = []
for i in range(len(data)-1):
    if (abs(data[i] - data[i+1]) % 2 == 0) and (abs(data[i] - data[i+1]) % 37 == 0):
        a.append(data[i]+data[i+1])

print(len(a),max(a)) 