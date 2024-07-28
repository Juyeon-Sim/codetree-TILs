n=int(input())
arr=[[0 for _ in range(n)] for _ in range(n)]
a=1

if n%2==0:
    for i in range(n-1, -1, -1):
        if i%2==1:
            for j in range(n-1, -1, -1):
                arr[j][i]=a
                a+=1
        else:
            for j in range(n):
                arr[j][i]=a
                a+=1
else:
    for i in range(n-1, -1, -1):
        if i%2==0:
            for j in range(n-1, -1, -1):
                arr[j][i]=a
                a+=1
        else:
            for j in range(n):
                arr[j][i]=a
                a+=1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()