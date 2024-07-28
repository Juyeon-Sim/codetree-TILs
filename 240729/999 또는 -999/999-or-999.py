arr=list(map(int, input().split()))
ma=arr[0]
mi=arr[0]
for i in range(1, len(arr)):
    if arr[i]==999 or arr[i]==-999:
        break
    if arr[i]>ma:
        ma=arr[i]
    if arr[i]<mi:
        mi=arr[i]
print("%d %d"%(ma, mi))