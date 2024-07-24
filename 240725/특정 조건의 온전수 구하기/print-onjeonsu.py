n=int(input())
a=0
for i in range(a, n+1):
    if i%2==0 or (i%5==0 and i%10!=0) or (i%3==0 and i%9!=0):
        pass
    else:
        print(i, end=' ')