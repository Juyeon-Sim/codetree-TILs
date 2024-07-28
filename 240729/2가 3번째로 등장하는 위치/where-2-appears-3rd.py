n=int(input())
arr=list(map(int, input().split()))
arr2=[]
for i in range(n):
    if arr[i]==2:
        arr2.append(i)
print(arr2[2]+1)