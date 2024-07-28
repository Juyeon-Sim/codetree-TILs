n=int(input())
arr=list(map(int, input().split()))
arr2=[]
a=0

for i in arr:
    if i%2==0:
        arr2.append(i)
        a+=0

for i in range(a, -1, -1):
    print(arr2[i], end=' ')