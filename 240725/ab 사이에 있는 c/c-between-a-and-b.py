satisfied=False

x=input().split()
a, b, c = int(x[0]), int(x[1]), int(x[2])

for i in range(a, b+1):
    if i%c==0:
        satisfied=True
if satisfied==True:
    print("YES")
else:
    print("NO")