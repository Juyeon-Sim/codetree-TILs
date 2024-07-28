arr=list(map(int, input().split()))
arr2=[0]*10
a,b=arr[0],arr[1]

while a>=1:
    x=a//b
    y=a%b
    a=x
    arr2[y]+=1

s=sum(i**2 for i in arr2)
print(s)