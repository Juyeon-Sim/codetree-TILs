n=int(input())
b=0

for _ in range(n):
    arr=list(map(int, input().split()))
    a=sum(arr)/4
    if a>=60:
        print("pass")
        b+=1
    else:
        print("fail")
print(b)