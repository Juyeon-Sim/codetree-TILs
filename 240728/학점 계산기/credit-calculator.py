n=int(input())
arr=list(map(float, input().split()))
a=sum(arr)/n
print("%.1f"%a)
if a>=4.0:
    print("Perfect")
elif a>=3.0:
    print("Good")
else:
    print("Poor")