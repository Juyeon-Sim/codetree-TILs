arr = input().split()
s = arr[0]
q = int(arr[1])

# 문자열을 리스트로 변환
ss = list(s)

for _ in range(q):
    a = int(input())
    
    if a == 1:
        # 첫 번째 문자를 마지막으로 이동
        ss = ss[1:] + [ss[0]]
        print(''.join(ss))
    elif a == 2:
        # 마지막 문자를 첫 번째로 이동
        ss = [ss[-1]] + ss[:-1]
        print(''.join(ss))
    elif a == 3:
        # 문자열을 반전
        print(''.join(ss[::-1]))