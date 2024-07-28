N=int(input())
a=0
for i in range(N):
    for j in range(N):
        if i>j:
            print(end='  ')
        else:
            print(chr(ord('A')+a), end=' ')
            a+=1
            if ord('A')+a>ord('Z'):
                a=0
    print()