arr2=[]
for _ in range(2):
    arr=list(map(int, input().split()))
    arr2.append(arr)
    print("%.1f"%(sum(arr)/4), end=' ')
print()

for i in range(4):
    s=0
    for j in range(2):
        s+=arr2[j][i]
    print("%.1f"%(s/2), end=' ')
print()

s=0
for i in range(4):
    for j in range(2):
        s+=arr2[j][i]
print("%.1f"%(s/8), end=' ')