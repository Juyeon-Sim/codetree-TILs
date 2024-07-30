arr=list(map(int, input().split()))
n=arr[0]
m=arr[1]

def fun(n, m):
    for _ in range(n):
        print('1'*m)

fun(n, m)