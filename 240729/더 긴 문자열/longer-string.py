arr=list(map(str, input().split()))
a,b=arr[0],arr[1]
if len(a)==len(b):
    print("same")
elif len(a)>len(b):
    print("%s %d"%(a, len(a)))
else:
    print("%s %d"%(b, len(b)))