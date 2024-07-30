arr=list(input().split())
n=int(arr[0])
A=str(arr[1])
cnt=0

for _ in range(n):
    a=str(input())
    if a==A:
        cnt+=1
print(cnt)