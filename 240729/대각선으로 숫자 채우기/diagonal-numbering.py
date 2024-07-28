x=list(map(int, input().split()))
n,m=x[0],x[1]
arr=[[0 for _ in range(m)] for _ in range(n)]
a=1

for i in range(n+m-1):
    for j in range(n):
        for k in range(m):
            if i==j+k:
                arr[j][k]=a
                a+=1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()