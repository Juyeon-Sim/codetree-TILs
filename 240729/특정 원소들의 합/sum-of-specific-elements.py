arr2=[]
for _ in range(4):
    arr=list(map(int, input().split()))
    arr2.append(arr)

s=0
for i in range(4):
    for j in range(4):
        if j>i:
            pass
        else:
            s+=arr2[i][j]
print(s)