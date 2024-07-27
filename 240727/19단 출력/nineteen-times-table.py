for i in range(1, 20):
    for j in range(1, 20):
        if j==19:
            print("%d * %d = %d"%(i, j, i*j), end='\n')
        elif j%2==1:
            print("%d * %d = %d /"%(i, j, i*j), end=' ')
        else:
            print("%d * %d = %d"%(i, j, i*j), end='\n')