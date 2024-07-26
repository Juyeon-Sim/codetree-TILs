n=int(input())
cnt=-n+1

for i in range(n):
    if i%2==0:
        cnt=cnt+n-1
        for j in range(n):
            cnt+=1
            print(cnt, end=' ')
    else:
        cnt=2*cnt+1
        for j in range(n):
            cnt-=1
            print(cnt, end=' ')
    print()