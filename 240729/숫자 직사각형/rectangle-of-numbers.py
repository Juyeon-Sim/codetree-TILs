arr=list(map(int, input().split()))
n=arr[0]
m=arr[1]
arr2=[[0 for _ in range(m)]for _ in range(n)]
a=1

for i in range(n):
    for j in range(m):
        arr2[i][j]=a
        print(a, end=' ')
        a+=1
    print()