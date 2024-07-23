a=input().split()
a1=str(a[0])
a2=int(a[1])

b=input().split()
b1=str(b[0])
b2=int(b[1])

c=input().split()
c1=str(c[0])
c2=int(c[1])

if (a1=="Y" and a2>=37) and (b1=="Y" and b2>=37):
    print("E")
elif (a1=="Y" and a2>=37) and (c1=="Y" and c2>=37):
    print("E")
elif (b1=="Y" and b2>=37) and (c1=="Y" and c2>=37):
    print("E")
else:
    print("N")