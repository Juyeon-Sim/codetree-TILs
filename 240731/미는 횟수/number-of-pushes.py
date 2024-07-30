A = input()
B = input()

# 문자열 회전 가능 여부 확인
if len(A) != len(B):
    print(-1)
else:
    # A+A에 B가 포함되는지 확인
    concatenated = A + A
    if B in concatenated:
        # B가 포함되는 위치를 찾아 회전 횟수 계산
        cnt = concatenated.index(B)
        print(cnt)
    else:
        print(-1)