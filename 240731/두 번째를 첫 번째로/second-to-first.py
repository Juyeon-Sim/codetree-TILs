s=list(input())
a=s[0]
b=s[1]
for i in range(len(s)):
    if s[i]==b:
        s[i]=a

for i in s:
    print(i, end='')