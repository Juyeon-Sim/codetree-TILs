arr=input().split()
a=int(arr[0])
b=int(arr[1])

for i in range(2, 9, 2):
    for j in range(b, a-1, -1):
        print("%d * %d = %d"%(j, i, i*j), end='')
        if j>a:
            print(" /", end=' ')
    print()