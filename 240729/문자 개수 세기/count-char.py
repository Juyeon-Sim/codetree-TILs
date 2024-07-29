string=input()
alph=input()
cnt=0
for i in range(len(string)):
    if string[i]==alph:
        cnt+=1
print(cnt)