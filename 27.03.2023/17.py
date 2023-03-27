data = open('17.txt')

data = [int(x) for x in data.read().split()]

a = []

for i in data:
    if i % 3 == 0 and i % 9 != 0 and int(str(i)[-1]) >= 4:
        a.append(i)

print(len(a), sum(a)/len(a))