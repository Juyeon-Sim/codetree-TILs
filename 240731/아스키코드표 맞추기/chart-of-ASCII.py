arr=list(map(int, input().split()))
arr2=[]

for i in range(len(arr)):
    arr2.append(chr(arr[i]))

for i in arr2:
    print(i, end=' ')