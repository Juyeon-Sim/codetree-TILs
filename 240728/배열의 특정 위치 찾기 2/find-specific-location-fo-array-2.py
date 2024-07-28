arr=list(map(int, input().split()))
arr2=[]
arr3=[]

for i in range(10):
    if i%2==0:
        arr2.append(arr[i])
    else:
        arr3.append(arr[i])

a=sum(arr2)
b=sum(arr3)

if a>b:
    print(a-b)
else:
    print(b-a)