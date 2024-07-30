n=int(input())
s=0
for _ in range(n):
    a=int(input())
    s+=a
ss=str(s)
ss=ss[1:]+ss[0]
for i in ss:
    print(i, end='')