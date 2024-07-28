x=list(map(int, input().split()))
n,m=x[0],x[1]
arr=[[0 for _ in range(m)] for _ in range(n)]
a=0

for i in range(m):
    if i%2==0:
        for j in range(n):
            arr[j][i]=a
            a+=1
    else:
        for j in range(n-1, -1, -1):
            arr[j][i]=a
            a+=1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()