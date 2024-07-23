x=input().split()
ay=int(x[0])
az=str(x[1])

y=input().split()
by=int(y[0])
bz=str(y[1])

if (ay>=19 and az=="M") or (by>=19 and bz=="M"):
    print(1)
else:
    print(0)