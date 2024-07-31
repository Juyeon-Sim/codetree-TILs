arr=list(map(int, input().split()))
a,b,c=arr[0],arr[1],arr[2]
def minimum(*args):
    return min(args)

print(int(minimum(a, b, c)))