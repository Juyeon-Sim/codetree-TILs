x=input().split()
a=int(x[0])
b=int(x[1])
print("%d."%(a//b), end='')
for i in range(20):
    a=(a%b)*10
    print("%d"%(a//b), end='')