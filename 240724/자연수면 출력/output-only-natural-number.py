x=input().split()
a=int(x[0])
b=int(x[1])

if a>0:
    for _ in range(b):
        print(a, end='')
else:
    print(0)