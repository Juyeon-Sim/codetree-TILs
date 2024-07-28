arr=list(map(int, input().split()))
cnt=0
a=0

for i in arr:
    if i==0:
        break
    cnt+=1

for i in range(cnt):
    a+=arr[i]

print("%d %.1f"%(a, a/cnt))