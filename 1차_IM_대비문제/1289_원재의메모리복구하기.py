T = int(input())

for tc in range(1, T + 1):
    memory = input()

    # 메모리가 1로 시작하면 초기화 상태에서 바꿔줘야하므로 count = 1
    if memory[0] == '1':
        count = 1
    else:
        count = 0

    # 메모리를 돌면서 숫자가 바꿔면 count ++
    for i in range(len(memory) - 1):
        if memory[i] != memory[i + 1]:
            count += 1

    print(f'#{tc}', count)

# -----------------------------------------------------------------
# 혜진 코드
T = int(input())
for test_case in range(1, T+1):
    memory = [0] + list(map(int, input()))      # 0에서 1로 바뀌는 걸로 시작해야하니까
    count = 0
    for i in range(len(memory)-1):
        if memory[i] != memory[i+1]:        # 뒤가 다르면 카운트
            count += 1
    print(f'#{test_case}', count)

# ------------------------------------------------------------------
# 성구 코드
for test_case in range(1, int(input())+1):
    memory = input()
    flag = 0        # 반전 표시
    cnt = 0             # 반전 횟수
    for i in range(len(memory)):
        if memory[i] != str(flag):  # 값이 다르면
            flag = 0 if flag else 1 # 반전
            cnt += 1                # 횟수 +1
    print(f'#{test_case} {cnt}')
