arr2=[0]*4

for i in range(3):
    arr=input().split()
    a=str(arr[0])
    b=int(arr[1])
    if b>=37:
        if a=='Y':
            arr2[0]+=1
        else :
            arr2[1]+=1
    else:
        if a=='Y':
            arr2[2]+=1
        else:
            arr2[3]+=1

for i in range(4):
    print(arr2[i], end=' ')

if arr2[0]>=2:
    print("E")