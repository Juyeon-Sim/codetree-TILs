n=int(input())
s,x=0,0

for _ in range(n):
    string=input()
    s+=len(string)
    if string[0]=='a':
        x+=1

print("%d %d"%(s, x))