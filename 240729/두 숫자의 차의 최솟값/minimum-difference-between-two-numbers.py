n=int(input())
arr=list(map(int, input().split()))
m=100
for i in range(n):
    for j in range(i+1, n):
        if abs(arr[i]-arr[j])<m:
            m=abs(arr[i]-arr[j])
print(m)