x=input().split()
a=int(x[0])
b=int(x[1])

for i in range(a):
    for j in range(b):
        print((i+1)*(j+1), end=' ')
    print()