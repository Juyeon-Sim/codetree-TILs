s=input()
ss=list(s)
L=len(s)

for i in ss:
    print(i, end='')
print()

for _ in range(L):
    ss=[ss[-1]]+ss[:L-1]
    for i in ss:
        print(i, end='')
    print()