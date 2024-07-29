arr=[input() for _ in range(10)]
arr2=[]
string=input()

for i in range(10):
    if arr[i][len(arr[i])-1]==string:
        arr2.append(arr[i])

if len(arr2)==0:
    print("None")
else:
    for i in range(len(arr2)):
        print(arr2[i])