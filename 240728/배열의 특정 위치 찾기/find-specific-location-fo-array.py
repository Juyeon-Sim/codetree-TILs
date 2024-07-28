arr=list(map(int, input().split()))
s=0
s2=0

for i in range(10):
    if i%2==1:
        s+=arr[i]

for i in range(1, 11):
    if i%3==0:
        s2+=arr[i-1]

a=s2/3
print("%d %.1f"%(s, a))