arr=input().split()
s=str(arr[0])
q=int(arr[1])
ss=list(s)

for i in range(q):
    a=int(input())
    if a==1:
        ss=ss[1:len(s)]+[ss[0]]
        for j in ss:
            print(j, end='')
        print()
        #0번을 마지막으로
    elif a==2:
        ss=[ss[len(s)-1]]+ss[:len(s)-1]
        for j in ss:
            print(j, end='')
        print()
        #마지막을 0번으로
    else:
        for j in range(len(s)-1, -1, -1):
            print(ss[j], end='')
        print()
        #반대로