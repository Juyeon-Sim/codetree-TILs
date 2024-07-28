n = int(input())
arr = [1, n]

while True:
    next_value = arr[-1] + arr[-2]
    if next_value > 100:
        break
    arr.append(next_value)

for value in arr:
    print(value, end=' ')
print(arr[-1]+arr[-2])