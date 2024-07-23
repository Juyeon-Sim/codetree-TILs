x=input().split()
h=int(x[0])
w=int(x[1])
b=(10000*w)/(h*h)
print("%d"%b)
if b>=25:
    print("Obesity")