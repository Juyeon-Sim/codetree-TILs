arr=list(map(int, input().split()))

m=arr[0]
for i in arr[1:]:
    if i>m:
        m=i
print(m)