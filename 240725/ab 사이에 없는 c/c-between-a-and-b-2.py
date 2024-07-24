satisfied=True

x=input().split()
a=int(x[0])
b=int(x[1])
c=int(x[2])

for i in range(a, b+1):
    if i%c==0:
        satisfied=False
if satisfied==True:
    print("YES")
else:
    print("NO")