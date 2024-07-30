arr=list(map(str, input().split()))
string=arr[0]
alph=arr[1]

if alph in string:
    print(string.find(alph))
else:
    print("No")