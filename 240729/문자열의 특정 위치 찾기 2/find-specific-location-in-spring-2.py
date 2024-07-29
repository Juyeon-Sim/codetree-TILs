arr=["apple", "banana", "grape", "blueberry", "orange"]
alph=input()
cnt=0

for i in range(5):
    if arr[i][2]==alph or arr[i][3]==alph:
        print(arr[i])
        cnt+=1
print(cnt)