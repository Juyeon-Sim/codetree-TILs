arr=input()
a, b=0, 0

for i in range(len(arr)-1):
    if arr[i]=='e' and arr[i+1]=='e':
        a+=1
    elif arr[i]=='e' and arr[i+1]=='b':
        b+=1

print("%d %d"%(a, b))