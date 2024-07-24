s=0
a=0
while True:
    n=int(input())
    if n<20 or n>29:
        print("%.2f"%(s/a))
        break
    s+=n
    a+=1