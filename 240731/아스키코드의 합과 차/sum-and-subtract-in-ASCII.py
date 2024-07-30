arr=list(map(str, input().split()))
a=ord(arr[0])
b=ord(arr[1])

if a>b:
    print("%d %d"%(a+b, a-b))
else:
    print("%d %d"%(a+b, b-a))