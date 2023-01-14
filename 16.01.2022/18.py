data = open('18.txt')

s = [int(x) for x in data.read().split()]

count = 0

for i in range(len(s)):
    try:
        if (s[i] + s[i+1] < 100) or (s[i] + s[i+2] < 100) or (s[i] + s[i+3] < 100) or (s[i] + s[i+4] < 100) or (s[i] + s[i+5] < 100):
            count += 1
    except IndexError:
        try:
            if (s[i] + s[i+1] < 100) or (s[i] + s[i+2] < 100) or (s[i] + s[i+3] < 100) or (s[i] + s[i+4] < 100):
                count += 1
        except IndexError:
            try:
                if (s[i] + s[i+1] < 100) or (s[i] + s[i+2] < 100) or (s[i] + s[i+3] < 100):
                    count += 1
            except IndexError:
                try:
                    if (s[i] + s[i+1] < 100) or (s[i] + s[i+2] < 100):
                        count += 1
                except IndexError:
                    count += 0


        


print(count)