arr=list(map(int, input().split()))
a=str(arr[0]+arr[1])
cnt=0

for i in range(len(a)):
    if a[i]=='1':
        cnt+=1
print(cnt)