arr=input().split()
s=int(arr[0])
e=int(arr[1])
b=0
for i in range(s, e+1):
    a=0
    for j in range(1, i+1):
        if i%j==0:
            a+=1
    if a==3:
        b+=1
print(b)