x=input().split()
a=int(x[0])
b=int(x[1])
s=0
n=0
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        s+=i
        n+=1
print(s, "%.1f"%(s/n))