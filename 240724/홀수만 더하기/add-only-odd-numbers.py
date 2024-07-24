n=int(input())
s=0
for i in range(n):
    n=int(input())
    if n%2==1 and n%3==0:
        s+=n
print(s)