x=input().split()
am=int(x[0])
ae=int(x[1])
y=input().split()
bm=int(y[0])
be=int(y[1])

if am>bm:
    print("A")
elif bm>am:
    print("B")
elif ae>be:
    print("A")
else:
    print("B")