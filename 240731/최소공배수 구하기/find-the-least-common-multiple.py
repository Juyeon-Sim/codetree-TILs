arr=list(map(int, input().split()))
n,m=arr[0],arr[1]

def fun(a,b):
    i=max(a, b)
    while True:
        if i%a==0 and i%b==0:
            print(i)
            break
        else:
            i+=1

fun(n, m)