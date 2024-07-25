n=int(input())

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n or j==n:
            for _ in range(n):
                print("*", end=' ')
        elif i<=j:
            print("*", end=' ')
        else:
            print(end='  ')
    print()