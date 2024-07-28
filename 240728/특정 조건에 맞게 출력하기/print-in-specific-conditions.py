arr=list(map(int, input().split()))
arr2=[]
i=0

while arr[i]!=0:
    if arr[i]%2==1:
        arr2.append(arr[i]+3)
    else:
        arr2.append(arr[i]//2)
    i+=1

for j in range(i):
    print(arr2[j], end=' ')