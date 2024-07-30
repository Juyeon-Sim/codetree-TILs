arr = list(input())

# 결과를 저장할 리스트
result = []

# 문자 범위에 따라 필터링
for char in arr:
    if 'a' <= char <= 'z':
        result.append(char)  # 소문자는 그대로 추가
    elif 'A' <= char <= 'Z':
        result.append(char.lower())  # 대문자는 소문자로 변환하여 추가
    elif char.isdigit():
        result.append(char)  # 숫자는 그대로 추가

# 결과를 문자열로 변환하여 출력
print(''.join(result))