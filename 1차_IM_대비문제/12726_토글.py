T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 문제에서 입력 받는 배열의 행, 렬이 1부터 시작하므로 맞춰줘야함
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    # M초 동안 반복
    for k in range(1, M + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):

                # M이 k의 배수일 경우
                if M % k == 0:
                    if arr[i][j]:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1
                # (2)번 조건. 어차피 i + j가 k와 같은 것은 k의 배수가 되는 것이다
                elif (i + j) % k == 0:
                    if arr[i][j]:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1

    # 최종적으로 만들어진 배열을 탐색하며 1이면 count ++
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j]:
                count += 1
    # print(arr)
    print(f'#{tc}', count)

