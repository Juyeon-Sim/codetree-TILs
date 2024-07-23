x=input().split()
a=int(x[0])
b=int(x[1])
c=int(x[2])

if (a<=b and b<=c) or (c<=b and b<=a):
    print(b)
elif (b<=a and a<=c) or (c<=a and a<=b):
    print(a)
else:
    print(c)