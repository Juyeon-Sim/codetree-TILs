arr=list(map(int, input().split()))
n=len(arr)
s, a= 0, 0
for i in range(n):
    if arr[i]>=250:
        break
    elif arr[i]<250:
        s+=arr[i]
        a+=1
print("%d %.1f"%(s, s/a))