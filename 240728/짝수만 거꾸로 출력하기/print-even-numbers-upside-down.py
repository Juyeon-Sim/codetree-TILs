n = int(input())  
arr = list(map(int, input().split()))  
arr2 = []  

for i in range(n):
    if arr[i] % 2 == 0:
        arr2.append(arr[i])

for i in range(len(arr2) - 1, -1, -1):
    print(arr2[i], end=' ')