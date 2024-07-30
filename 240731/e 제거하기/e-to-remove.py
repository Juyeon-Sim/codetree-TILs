s=input()
ss=list(s)

ss=ss[:ss.index('e')]+ss[ss.index('e')+1:]

for i in ss:
    print(i, end='')