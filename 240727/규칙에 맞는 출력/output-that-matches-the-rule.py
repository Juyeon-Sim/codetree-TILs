N=int(input())

for i in range(N):
    for j in range(N):
        if j>i:
            pass
        else:
            print(j+N-i, end=' ')
    print()