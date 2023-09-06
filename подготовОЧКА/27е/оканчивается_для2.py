data = open('27-B_637.txt')
n = data.readline()
s = [0]
maxim =0
for i in data.readlines():
    pairs = [int(x) for x in i.split()]
    s = [a+b for a in s for b in pairs]
    s = {x % 10: x for x in sorted(s)}.values()

for i in s:
    if i % 10 != 5:
        maxim = max(maxim, i)

print(maxim)