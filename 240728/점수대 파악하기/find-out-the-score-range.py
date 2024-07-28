arr=list(map(int, input().split()))
n=len(arr)

for i in range(10, 0, -1):
    cnt=0
    for j in range(n):
        if arr[j]==0:
            break
        if i==(arr[j]//10):
            cnt+=1
    print("%d - %d"%(i*10, cnt))