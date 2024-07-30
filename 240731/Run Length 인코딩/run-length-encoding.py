A=input()
arr=[]
arr1=[]
length=len(A)

for i in range(length):
    if i==0:
        arr.append(A[i])
        cnt=1
    elif i==length-1:
        if A[i]==A[i-1]:
            arr.append(A[i])
            cnt+=1
            arr.append(cnt)
        else:
            arr.append(cnt)
            arr.append(A[i])
            cnt=1
            arr.append(cnt)
    elif A[i]==A[i-1]:
        arr.append(A[i])
        cnt+=1
    else:
        arr.append(cnt)
        arr.append(A[i])
        cnt=1

for i in range(len(arr)):
    if arr[i]==arr[i-1]:
        pass
    else:
        arr1.append(arr[i])

print(len(arr1))
for i in arr1:
    print(i, end='')