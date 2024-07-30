s=input()
ss=list(s)
co=input()

for i in range(len(co)):
    if co[i]=='L':
        ss=ss[1:]+[ss[0]]
    else:
        ss=[ss[-1]]+ss[:len(s)-1]

for i in ss:
    print(i, end='')