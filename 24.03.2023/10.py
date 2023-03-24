data = open('10.txt')

data = data.read().split()
count = 0
for i in data:
    if ('в' in i or 'В' in i) and 'а' not in i and 'о' not in i and 'А' not in i and 'О' not in i:
        print(i)
        count += 1
print(count)