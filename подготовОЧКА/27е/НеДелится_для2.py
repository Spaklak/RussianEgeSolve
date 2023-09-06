data = open('27-A_814.txt')
n = int(data.readline())
s = [0]
for i in data.readlines():
    pairs = [int(x) for x in i.split()]
    s = [a+b for a in s for b in pairs]
    s = {x%5: x for x in (sorted(s)[::-1])}.values()

solve = 10000000000
for i in s:
    if i % 5 != 0:
        solve = min(i,solve)

print(solve)