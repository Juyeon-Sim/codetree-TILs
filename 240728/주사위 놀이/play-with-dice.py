arr=list(map(int, input().split()))

for i in range(1, 7):
    cnt=0
    for j in range(10):
        if arr[j]==i:
            cnt+=1
    print("%d - %d"%(i, cnt))