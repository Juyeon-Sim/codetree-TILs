x=input().split()
a=int(x[0])
b=int(x[1])
s=1
for _ in range(b):
    s*=a
print(s)