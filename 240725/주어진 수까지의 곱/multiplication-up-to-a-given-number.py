x=input().split()
a=int(x[0])
b=int(x[1])
s=1
for i in range(a, b+1):
    s*=i
print(s)