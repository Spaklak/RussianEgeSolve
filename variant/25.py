for i in range(190201, 190260):
    spisokDelitelei = []
    for x in range(1, i + 1):
        if i % x == 0 and x % 2 == 0:
            spisokDelitelei.append(x)
    if len(spisokDelitelei) == 4:
        spisokDelitelei.sort()
        print(spisokDelitelei[3], spisokDelitelei[2])