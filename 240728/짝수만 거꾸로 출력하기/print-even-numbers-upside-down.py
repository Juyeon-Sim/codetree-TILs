n=int(input())
arr=list(map(int, input().split()))
arr2=[]
a=0

for i in range(n):
    for j in arr:
        if j%2==0:
            arr2.append(i)
            a+=1

for i in range(a-1, -1, -1):
    print(arr2[j], end=' ')