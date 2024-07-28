n=int(input())
a=0
for i in range(n):
    for j in range(n):
        if j>i:
            print(end='')
        else:
            print(chr(ord('A')+a), end='')
            a+=1
            if ord('A')+a>ord('Z'):
                a=0
    print()