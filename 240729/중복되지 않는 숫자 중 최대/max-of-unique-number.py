N = int(input())
arr = list(map(int, input().split()))

# 중복을 추적하기 위한 두 리스트
unique_arr = []
duplicates = []

# 중복 요소 제거 및 리스트 생성
for num in arr:
    if num in unique_arr:
        duplicates.append(num)
    else:
        unique_arr.append(num)

# 중복된 요소 제거
result_arr = [num for num in unique_arr if num not in duplicates]

# 중복 제거 후 리스트가 비었는지 확인
if len(result_arr) == 0:
    print(-1)
else:
    # 최대값 출력
    print(max(result_arr))