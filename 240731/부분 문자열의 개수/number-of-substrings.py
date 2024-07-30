A=input()
B=input()
cnt=0

for i in range(len(A)-len(B)+1):
    a=0
    for j in range(len(B)):
        if A[i+j]==B[j]:
            a+=1
    if a==len(B):
        cnt+=1

print(cnt)