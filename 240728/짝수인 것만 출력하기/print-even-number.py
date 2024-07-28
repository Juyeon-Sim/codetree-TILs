n=int(input())
arr=list(map(int, input().split()))
arr2=[]
a=0

for i in range(n):
    if arr[i]%2==0:
        arr2.append(arr[i])
        a+=1

for i in range(a):
    print(arr2[i], end=' ')