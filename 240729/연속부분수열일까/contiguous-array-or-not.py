arr_n1n2=list(map(int, input().split()))
arr_A=list(map(int, input().split()))
arr_B=list(map(int, input().split()))
n1,n2=arr_n1n2[0],arr_n1n2[1]

a=arr_B[0]
b=arr_A.index(a)
arr=[]

for i in range(b, b+n2+1):
    arr.append(arr_A[i])

if arr==arr_B:
    print("Yes")
else:
    print("No")