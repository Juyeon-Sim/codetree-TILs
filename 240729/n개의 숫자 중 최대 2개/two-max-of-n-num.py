N=int(input())
arr=list(map(int, input().split()))

for i in range(N):
    for j in range(N-i-1):
        if arr[j]<arr[j+1]:
            arr[j], arr[j+1]=arr[j+1], arr[j]
print("%d %d"%(arr[0], arr[1]))