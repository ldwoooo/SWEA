T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(N):
            fly1 = arr[i][j]
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                for m in range(1, M):
                    ni, nj = i + di * m, j + dj * m
                    if (0 <= ni < N) and (0 <= nj < N):
                        fly1 += arr[ni][nj]

            if maxV < fly1:
                maxV = fly1

    for i in range(N):
        for j in range(N):
            fly2 = arr[i][j]
            for di, dj in [[1, 1], [-1, -1], [1, -1], [-1, 1]]:
                for m in range(1, M):
                    ni, nj = i + di * m, j + dj * m
                    if (0 <= ni < N) and (0 <= nj < N):
                        fly2 += arr[ni][nj]
            if maxV < fly2:
                maxV = fly2

    print(f'#{tc}', maxV)
