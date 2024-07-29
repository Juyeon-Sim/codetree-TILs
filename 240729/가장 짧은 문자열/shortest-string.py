a, b, c=input(), input(), input()
m,n=0,0

for _ in range(3):
    if len(a)<=len(b) and len(a)<=len(c):
        n=len(a)
    elif len(b)<=len(a) and len(b)<=len(c):
        n=len(b)
    else:
        n=len(c)
    if len(a)>=len(b) and len(a)>=len(c):
        m=len(a)
    elif len(b)>=len(a) and len(b)>=len(c):
        m=len(b)
    else:
        m=len(c)
print(m-n)