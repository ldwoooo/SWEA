T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    fly = 0
    maxV = 0                                # 비교하며 최댓값 구하기
    # stack = []                            # stack 활용해서 최댓값 구하기
    for i in range(N - (M - 1)):            # 큰 범위 배열 탐색
        for j in range(N - (M - 1)):
            fly = 0
            for k in range(i, i + M):       # 파리채 범위 배열 탐색
                for l in range(j, j + M):
                    fly += arr[k][l]        # 잡은 파리수 더해주기

            if maxV < fly:                  # 최댓값 구하기
                maxV = fly

            # stack.append(fly)

    # print(f'#{tc}', max(stack))
    print(f'#{tc}', maxV)