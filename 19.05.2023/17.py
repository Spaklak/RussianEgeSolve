data = open('17.txt')
data = [int(x) for x in data.read().split()]
letters = {}
maxlet = 0
symbol = 0
solve = []
for i in data:
    i = str(abs(i))
    if len(i) == 3:
        if i[1] not in letters:
            letters[i[1]] = 1
        else:
            letters[i[1]] = letters[i[1]] + 1

for i in letters:
    if letters[i] > maxlet:
        symbol = i
        maxlet = letters[i]

for i in range(len(data)-1):
    if str(data[i])[-1] == symbol or str(data[i+1])[-1] == symbol:
        solve.append(data[i] + data[i+1])

print(len(solve), max(solve))