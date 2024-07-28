n=int(input())
a=0
for i in range(n):
    for j in range(n):
        print(chr(ord('A')+a))
        a+=1