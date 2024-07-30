arr=input()
arr1=[]

for i in range(len(arr)):
    if i%2==1:
        arr1.append(arr[i])

for i in range(len(arr1)-1, -1, -1):
    print(arr1[i], end='')