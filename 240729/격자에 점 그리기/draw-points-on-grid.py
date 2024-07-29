arr=list(map(int, input().split()))
n,m=arr[0],arr[1]
a=1

placed=[[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c=tuple(map(int, input().split()))
    placed[r-1][c-1]=a
    a+=1

for i in placed:
    for j in i:
        print(j, end=' ')
    print()