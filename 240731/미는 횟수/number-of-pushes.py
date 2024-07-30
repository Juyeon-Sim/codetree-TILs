A = input()
B = input()

# 문자열 회전 가능 여부 확인
if len(A) != len(B):
    print(-1)
else:
    cnt = 0
    found = False
    original_A = A
    
    for _ in range(len(A)):
        if A == B:
            found = True
            break
        A = A[-1] + A[:-1]
        cnt += 1
    
    if found:
        print(cnt)
    else:
        print(-1)