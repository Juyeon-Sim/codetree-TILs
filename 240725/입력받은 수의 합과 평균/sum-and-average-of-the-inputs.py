n=int(input())
s=0
for _ in range(n):
    a=int(input())
    s+=a
print(s, "%.1f"%(s/n))