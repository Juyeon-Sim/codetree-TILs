x=input().split()
a=int(x[0])
b=int(x[1])
c=int(x[2])
if a<=b and a<=c:
    n=1
else:
    n=0
if a==b and a==c:
    m=1
else:
    m=0
print(n, m)