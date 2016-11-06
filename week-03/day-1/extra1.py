for i in range(1, -6, -6):
    for j in range(abs(i), 5+i, int(abs(i) / i) ):
        print('*' * j)
