n=int(input())
arr=[[0 for _ in range(n)] for _ in range(n)]
a=1

for i in range(n):
    for j in range(n):
        arr[j][i]=a
        a+=1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()