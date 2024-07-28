arr=list(map(int, input().split()))

for i in range(2, 11):
    if arr[-1]+arr[-2]>9:
        a=(arr[-1]+arr[-2])%10
        arr.append(a)
    else:
        b=(arr[-1]+arr[-2])
        arr.append(arr[-1]+arr[-2])

for i in range(10):
    print(arr[i], end=' ')