N=int(input())

def fun(N):
    cnt=0
    for i in range(1, N+1):
        cnt+=i
    return cnt//10

print(fun(N))