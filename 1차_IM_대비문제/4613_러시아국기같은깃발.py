T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    minV = 2500                                 # N x M 최대값

    # 3개의 영역으로 나누기
    for a in range(N - 2):                      # W영역 맨 아래 0 ~ N - 3
        for b in range(a + 1, N - 1):           # B 영역 맨 아래 a + 1 ~ N - 2
            count = 0                           # 각 영역에서 새로 칠하는 횟수
            for i in range(a + 1):              # W 영역에서 
                for j in range(M):
                    if flag[i][j] != 'W':       # 다른 색의 개수
                        count += 1
            for i in range(a + 1, b + 1):       # B 영역에서
                for j in range(M):
                    if flag[i][j] != 'B':       # 다른 색의 개수
                        count += 1
            for i in range(b + 1, N):           # R 영역에서
                for j in range(M):
                    if flag[i][j] != 'R':       # 다른 색의 개수
                        count += 1

            if minV > count:
                minV = count

    print(f'#{tc}', minV)