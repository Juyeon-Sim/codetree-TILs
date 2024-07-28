arr1=list(map(int, input().split()))
n,q=arr1[0],arr1[1]
arr2=list(map(int, input().split()))
for i in range(q):
    arr3=list(map(int, input().split()))
    if arr3[0]==1:
        print(arr2[arr3[1]-1])
    elif arr3[0]==2:
        if arr3[1] not in arr2:
            print(0)
        else:
            arr4=[]
            arr4.append(arr2.index(arr3[1])+1)
            print(arr4[0])
    else:
        for j in range(arr3[1]-1, arr3[2]):
            print(arr2[j], end=' ')