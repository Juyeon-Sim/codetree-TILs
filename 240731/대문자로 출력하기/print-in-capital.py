arr=list(input())

for i in range(len(arr)):
    if ord('A')<=ord(arr[i])<=ord('Z'):
        pass
    elif ord('a')<=ord(arr[i])<=ord('z'):
        arr[i]=arr[i].upper()
    else:
        arr[i]=''
for i in arr:
    print(i, end='')