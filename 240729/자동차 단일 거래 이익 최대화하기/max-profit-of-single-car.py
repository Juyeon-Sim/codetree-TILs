n = int(input())
arr = list(map(int, input().split()))

# 배열이 내림차순으로 정렬된 경우 확인
is_descending = True
for i in range(n-1):
    if arr[i] <= arr[i+1]:
        is_descending = False
        break

if is_descending:
    print(0)
else:
    max_diff = -1
    # 최대 차이 찾기
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                diff = arr[j] - arr[i]
                if diff > max_diff:
                    max_diff = diff
    print(max_diff)