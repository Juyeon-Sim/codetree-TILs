A = input()
arr = []
length = len(A)

if length == 0:
    print(0)
else:
    current_char = A[0]
    cnt = 1
    
    for i in range(1, length):
        if A[i] == current_char:
            cnt += 1
        else:
            arr.append(current_char)
            arr.append(str(cnt))
            current_char = A[i]
            cnt = 1
    
    # 마지막 문자 처리
    arr.append(current_char)
    arr.append(str(cnt))
    
    # 결과 리스트의 길이 출력
    print(len(arr))
    
    # 결과 출력
    for element in arr:
        print(element, end='')