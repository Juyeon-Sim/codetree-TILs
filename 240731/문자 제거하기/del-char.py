s=input()
arr=list(s)
cnt=0
for _ in range(len(s)-1):
    n=int(input())
    if n>(len(s)-cnt-1):
        arr.pop(-1)
        cnt+=1
        for i in arr:
            print(i, end='')
        print()
    else:
        arr.pop(n)
        cnt+=1
        for i in arr:
            print(i, end='')
        print()