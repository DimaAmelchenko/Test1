d = [0.3, 1998, -5]

N = len(d)

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if d[j] > d[j + 1]:
            d[j], d[j + 1] = d[j + 1], d[j]
            print(d)
