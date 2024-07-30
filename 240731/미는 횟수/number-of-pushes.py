A=str(input())
B=str(input())
cnt=0

while True:
    if A==B:
        break
    else:
        A=A[-1]+A[:len(A)-1]
        cnt+=1

print(cnt)