N=int(input())
arr=list(map(int, input().split()))
m=arr[0]
for i in arr[1:]:
    if m>i:
        m=i

print("%d %d"%(m, arr.count(m)))