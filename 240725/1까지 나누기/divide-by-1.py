n=int(input())
s=0
for i in range(1, n +2):
    n=n//i
    s+=1
    if n<=1:
        print(s)
        break