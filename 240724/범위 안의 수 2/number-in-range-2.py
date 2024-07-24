s=0
a=0
for _ in range(10):
    n=int(input())
    if n>=0 and n<=200:
        s+=n
        a+=1
print(s, "%.1f"%(s/a))