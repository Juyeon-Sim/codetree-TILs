x=input().split()
a=int(x[0])
b=int(x[1])
s=0
if a<b:
    for i in range(a, b+1):
        if i%5==0:
            s+=i
else:
    for i in range(b, a+1):
        if i%5==0:
            s+=i
print(s)