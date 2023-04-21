import codecs

t = codecs.open('10.txt', 'r', 'utf_8_sig')
k = t.read().split()
count = 0
for data in k:
    data = data.replace('"', ' ')
    data = data.replace('.', ' ')
    data = data.replace(',', ' ')
    data = data.replace(':', ' ')
    data = data.replace(';', ' ')
    data = data.replace('?', ' ')
    data = data.replace('-', ' ')
    data = data.replace('(', ' ')
    data = data.replace(')', ' ')
    data = data.replace('/', ' ')
    data = data.replace('!', ' ')
    data = data.replace('—', ' ')
    data = data.replace('*', ' ')
    if len(data) > 1:
        count += 1
print(count)