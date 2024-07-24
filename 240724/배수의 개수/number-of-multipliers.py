a=0
b=0
c=0
for i in range(10):
    n=int(input())
    if n%15==0:
        a+=1
    elif n%3==0:
        b+=1
    elif n%5==0:
        c+=1
print(a+b, a+c)