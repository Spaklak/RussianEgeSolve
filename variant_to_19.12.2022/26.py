data = open('26.txt')
spisok = [int(x) for x in data.read().split()]
spisok = sorted(spisok)
for i in range(50):
    spisok.pop(0)
    spisok.pop()

average = (sum(spisok)/len(spisok))
print(max(spisok), average)