arr=list(map(int, input().split()))
cnt=0
s=0

for i in arr:
    if i==0:
        break
    elif i%2==0:
        s+=i
        cnt+=1
print("%d %d"%(cnt, s))