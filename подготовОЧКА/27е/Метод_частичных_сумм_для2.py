data = open('27-B_23.txt')
n = data.readline()
s=[0]
solve = 0
for i in data.readlines():
    pirs = [int(x) for x in i.split()]
    s = [a+b for a in s for b in pirs]
    s = {x % 3: x for x in sorted(s)}.values()

for i in s:
    if i % 3 != 0:
        solve = max(solve, i)

print(solve)