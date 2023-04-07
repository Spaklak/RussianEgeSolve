data = open('24.txt').read()
countf = 0
count = 0
for i in data:
    count += 1
    if i == 'f':
        countf += 1
        if countf == 123:
            print(count)
            break