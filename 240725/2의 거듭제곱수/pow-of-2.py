N=int(input())
x=0
while True:
    if N==1:
        break
    N=N//2
    x+=1
print(x)