N = int(input())
arr = list(map(int, input().split()))

indices = []

while len(arr) > 0:
    max_value = arr[0]
    max_index = 0
    
    # 최댓값과 그 인덱스 찾기
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    
    # 1-based index로 저장
    indices.append(max_index + 1)
    
    # 최댓값의 위치보다 왼쪽 부분을 남김
    arr = arr[:max_index]

# 결과 출력
for index in indices:
    print(index, end=' ')