n=int(input())

for i in range(n):
    for j in range(n):
        print("%d * %d = %d"%(i+1, j+1, (i+1)*(j+1)), end='')
        if j<n-1:
            print(",", end=' ')
    print()