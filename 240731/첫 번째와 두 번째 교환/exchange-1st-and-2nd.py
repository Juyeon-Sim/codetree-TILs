arr=list(input())
a=arr[0]
b=arr[1]

for i in range(len(arr)):
    if arr[i]==a:
        arr[i]=b
    elif arr[i]==b:
        arr[i]=a

for i in arr:
    print(i, end='')