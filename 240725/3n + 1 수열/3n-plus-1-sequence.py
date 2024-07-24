N=int(input())
a=0
while True:
    if N%2==0:
        N=N//2
        a+=1
    elif N%2==1 and N!=1:
        N=N*3+1
        a+=1
    elif N==1:
        print(a)
        break