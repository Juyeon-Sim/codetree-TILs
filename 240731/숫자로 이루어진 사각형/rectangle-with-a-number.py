N=int(input())

def fun(n):
    cnt=1
    for i in range(n):
        for j in range(n):
            if cnt==10:
                cnt=1
            print(cnt, end=' ')
            cnt+=1
        print()

fun(N)