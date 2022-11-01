for i in range(333555,777999+1):
    count = 0
    a = []
    for x in range(10,100):
        if i % x == 0:
            count += 1
            a.append(x)
    if count == 35:
        print(min(a),max(a))
        