arr=list(map(int, input().split()))
n=len(arr)

for i in range(1, 10):
    cnt=0
    for j in range(n):
        if i*10<=arr[j]<(i+1)*10:
            cnt+=1
    print("%d - %d"%(i, cnt))