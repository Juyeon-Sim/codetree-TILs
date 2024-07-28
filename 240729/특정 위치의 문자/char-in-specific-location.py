arr=['a']*6
arr=['L', 'E', 'B', 'R', 'O', 'S']
a=str(input())

if a not in arr:
    print("None")
else:
    print(arr.index(a))