n=int(input())
arr=[input() for _ in range(n)]
string=input()
s,a=0,0

for i in range(n):
    if arr[i][0]==string:
        s+=len(arr[i])
        a+=1

print("%d %.2f"%(a, s/a))