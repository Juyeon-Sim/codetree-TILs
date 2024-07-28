n=int(input())
arr=[]
a=0
b=0
i=1

while a<=2:
    arr.append(n*i)
    i+=1
    b+=1
    if (n*i)%5==0:
        a+=1

for i in range(b):
    print(arr[i], end=' ')