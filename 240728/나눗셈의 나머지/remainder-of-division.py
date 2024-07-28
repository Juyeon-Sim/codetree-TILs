arr=list(map(int, input().split()))
a,b=arr[0],arr[1]
arr2=[0]*b

while a>=1:
    x=a//b
    y=a%b
    a=x
    arr2[y]+=1

s=sum(i**2 for i in arr2)
print(s)