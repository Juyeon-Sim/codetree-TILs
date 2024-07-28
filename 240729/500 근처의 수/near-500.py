arr=list(map(int, input().split()))
mi=1000
ma=0
for i in arr:
    if i>500:
        if i<mi:
            mi=i
    else:
        if i>ma:
            ma=i
print("%d %d"%(ma, mi))