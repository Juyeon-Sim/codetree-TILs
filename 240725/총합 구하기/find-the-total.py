x=input().split()
a=int(x[0])
b=int(x[1])
s=0
for i in range(a, b+1):
    if i%6==0 and i%8!=0:
        s+=i
print(s)