data = open('17.txt')
data = [int(x) for x in data.read().split()]
count = []
minim = -1000000000000

for i in range(len(data)):
    if len(str(data[i])) == 3:
        minim = max(minim, data[i])



for i in range(len(data)-1):
    if (len(str(data[i])) == 3 and len(str(data[i+1])) != 3) or (len(str(data[i])) != 3 and len(str(data[i+1])) == 3):
        if (data[i] * data[i+1]) % minim == 0:
            print(data[i]*data[i+1])
            count.append(data[i]*data[i+1])

print(len(count), min(count))