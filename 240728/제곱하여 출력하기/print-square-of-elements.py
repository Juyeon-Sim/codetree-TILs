n=int(input())
arr=list(map(int, input().split()))
arr2=[arr[i]**2 for i in range(n)]
for i in range(n):
    print(arr2[i], end=' ')