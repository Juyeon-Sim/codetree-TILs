m=int(input())
for _ in range(m):
    n=int(input())
    a=0
    while n!=1:
        if n%2==0:
            n=n//2
            a+=1
        else:
            n=n*3+1
            a+=1
    print(a)