arr=list(input())

for i in range(len(arr)):
    if ord('a')<=ord(arr[i])<=ord('z'):
        arr[i]=arr[i].upper()
    else:
        arr[i]=arr[i].lower()

for i in arr:
    print(i, end='')