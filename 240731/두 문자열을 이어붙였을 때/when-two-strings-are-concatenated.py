a=input()
b=input()

ab=a+b
ba=b+a

cnt=0

for i in range(len(ab)):
    if ab[i]==ba[i]:
        cnt+=1

if cnt==len(ab):
    print("true")
else:
    print("false")