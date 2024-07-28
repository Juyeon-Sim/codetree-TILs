n=int(input())
arr=list(map(int, input().split()))
cnt=0
m=-1

for i in range(n-1):
    if arr[i]>arr[i+1]:
        cnt+=1
if cnt==n-1:
    print(0)
else:
    for i in range(0, n-1):
        for j in range(i, n):
            if arr[j]>arr[i] and (arr[j]-arr[i])>m:
                m=arr[j]-arr[i]
    print(m)