str1 = input()
str2 = input()

a = ''
b = ''

# 첫 번째 문자열에서 숫자만 추출합니다.
for char in str1:
    if '0' <= char <= '9':
        a += char

# 두 번째 문자열에서 숫자만 추출합니다.
for char in str2:
    if '0' <= char <= '9':
        b += char

# 추출된 숫자를 정수로 변환합니다.
n = int(a) if a else 0
m = int(b) if b else 0

# 두 숫자의 합을 출력합니다.
print(n + m)