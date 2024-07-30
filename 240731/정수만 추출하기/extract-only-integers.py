arr = input()

# 문자열을 수동으로 분리
n = ''
m = ''
is_second = False

for char in arr:
    if char == ' ':
        is_second = True
        continue
    if is_second:
        m += char
    else:
        n += char

# 함수 없이 숫자 추출 및 변환
def extract_number(s):
    number_str = ''
    for char in s:
        if char.isdigit():
            number_str += char
        else:
            break
    return int(number_str) if number_str else 0

# 첫 번째와 두 번째 문자열에서 숫자를 추출
a = extract_number(n)
b = extract_number(m)

# 결과를 출력합니다.
print(a + b)