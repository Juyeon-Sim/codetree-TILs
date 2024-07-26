n=int(input())
cnt=2

for i in range(n):
    for j in range(n):
        print(cnt, end=' ')
        if cnt==8:
            cnt=0
        cnt+=2
    print()