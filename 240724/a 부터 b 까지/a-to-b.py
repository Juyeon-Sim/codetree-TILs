x=input().split()
a=int(x[0])
b=int(x[1])

i=a
while i<=b:
    print(i, end=' ')
    if i%2==1:
        i*=2
    else:
        i+=3