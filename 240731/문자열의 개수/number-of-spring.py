cnt=0
arr=[]
arr2=[]
while True:
    a=str(input())
    if a=='0':
        break
    else:
        cnt+=1
        arr.append(a)

print(cnt)

for i in range(len(arr)):
    if i%2==0:
        arr2.append(arr[i])

for i in arr2:
    print(i)