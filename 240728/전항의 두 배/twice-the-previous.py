arr=list(map(int, input().split()))

for _ in range(8):
    arr.append(arr[-1]+arr[-2]*2)

for i in range(10):
    print(arr[i], end=' ')