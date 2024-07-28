arr_n1n2 = list(map(int, input().split()))
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
n1, n2 = arr_n1n2[0], arr_n1n2[1]

# arr_B가 arr_A의 부분 배열인지 확인
is_subarray = False

for i in range(n1 - n2 + 1):
    if arr_A[i:i + n2] == arr_B:
        is_subarray = True
        break

if is_subarray:
    print("Yes")
else:
    print("No")