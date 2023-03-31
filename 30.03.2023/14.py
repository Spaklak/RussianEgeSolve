a = 16 ** 20 + 2 ** 30 - 32
l = []
while a:
    l.append(a % 4)
    a//=4
print(l.count(3))