for _ in range(5):
    arr=list(map(str, input().split()))
    arr2=[i.upper() for i in arr]
    for j in range(3):
        print(arr2[j], end=' ')
    print()