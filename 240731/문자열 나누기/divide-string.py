n=int(input())
a=input()
string=''
for i in range(len(a)):
    if a[i]==' ':
        pass
    else:
        string+=a[i]

for i in range(len(string)):
    if (i+1)%5==0:
        print(string[i], end='\n')
    else:
        print(string[i], end='')