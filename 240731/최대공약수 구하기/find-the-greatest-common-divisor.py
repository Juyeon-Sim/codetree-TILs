arr=list(map(int, input().split()))
n,m=arr[0],arr[1]

def fun(a, b):
    if a>b:
        for i in range(a+1, 0, -1):
            if a%i==0 and b%i==0:
                print(i)
                break
    else:
        for i in range(b+1, 0, -1):
            if a%i==0 and b%i==0:
                print(i)
                break

fun(n, m)