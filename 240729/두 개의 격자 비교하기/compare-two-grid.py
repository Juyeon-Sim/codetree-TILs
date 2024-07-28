arr=list(map(int, input().split()))
n,m=arr[0],arr[1]
arr3=[]
arr4=[]
arr5=[[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    arr2=list(map(int, input().split()))
    arr3.append(arr2)
for _ in range(n):
    arr2=list(map(int, input().split()))
    arr4.append(arr2)

for i in range(n):
    for j in range(m):
        if arr3[i][j]==arr4[i][j]:
            arr5[i][j]=0
        else:
            arr5[i][j]=1

for i in arr5:
    for j in i:
        print(j, end=' ')
    print()