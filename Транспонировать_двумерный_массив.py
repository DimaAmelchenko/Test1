a = [[-5, 0.3, 1998], [5.5, -3.3, 19.98]]
b = [
    [ a[j][i] for j in range( len(a) ) ] for i in range( len(a[0]) )
    ]
print(b)


