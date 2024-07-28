n = int(input())
arr = []
a = 0
i = 1

while a < 2:
    multiple = n * i
    arr.append(multiple)
    if multiple % 5 == 0:
        a += 1
    i += 1

for value in arr:
    print(value, end=' ')