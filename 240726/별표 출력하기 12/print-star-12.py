n=int(input())

for i in range(n):
    if i==0:
        for _ in range(n):
            print("*", end=' ')
    else:
        for j in range(n):
            if j%2==1:
                print("*", end=' ')
            else:
                print("  ")
    print()