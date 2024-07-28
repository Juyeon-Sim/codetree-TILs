arr2=[]
arr3=[]
arr4=[[0 for _ in range(3)] for _ in range(3)]
for _ in range(3):
    arr=list(map(int, input().split()))
    arr2.append(arr)
n=input()
for _ in range(3):
    arr=list(map(int, input().split()))
    arr3.append(arr)

for i in range(3):
    for j in range(3):
        arr4[i][j]=arr2[i][j]*arr3[i][j]

for i in arr4:
    for j in i:
        print(j, end=' ')
    print()