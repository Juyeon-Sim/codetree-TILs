n=int(input())
def fun(i):
    return i%2==0 and ((i%10)+(i//10))%5==0

print("Yes" if fun(n) else "No")