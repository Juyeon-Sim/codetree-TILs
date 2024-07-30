arr = input().split()
s = arr[0]
q = int(arr[1])

for _ in range(q):
    arr2 = input().split()
    command = int(arr2[0])
    
    if command == 1:
        a = int(arr2[1])
        b = int(arr2[2])
        # 문자열을 리스트로 변환하여 인덱스를 교환합니다.
        s_list = list(s)
        s_list[a], s_list[b] = s_list[b], s_list[a]
        s = ''.join(s_list)
        print(s)
    
    elif command == 2:
        x = arr2[1]
        y = arr2[2]
        # 문자열을 리스트로 변환하여 문자를 대체합니다.
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == x:
                s_list[i] = y
        s = ''.join(s_list)
        print(s)