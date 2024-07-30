A = input()
B = input()

# 문자열 B의 길이
lenB = len(B)

# 문자열 A를 리스트로 변환하여 처리
listA = list(A)

# 결과를 저장할 리스트
result = []

i = 0
while i < len(listA):
    # 현재 인덱스에서 B가 일치하는지 검사
    if listA[i:i + lenB] == list(B):
        # B와 일치하면 B의 길이만큼 건너뜁니다.
        i += lenB
    else:
        # 일치하지 않으면 결과에 현재 문자를 추가합니다.
        result.append(listA[i])
        i += 1

# 리스트를 문자열로 변환하여 출력합니다.
print(''.join(result))