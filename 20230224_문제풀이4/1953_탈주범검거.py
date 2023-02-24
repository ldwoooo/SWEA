# def dfs():





T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]              # 상하좌우
    dj = [0, 0, -1, 1]

    up = [1, 2, 5, 6]               # 상하좌우에 따라 올 수 있는 파이프
    down = [1, 2, 4, 7]
    left = [1, 3, 4, 5]
    right = [1, 3, 6, 7]

    #  인접행렬
    adj = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if tunnel[i][j]:
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]

                    if (0 <= ni < N) and (0 <= nj < M) and tunnel[ni][nj]:
                        if (k == 0) and (tunnel[ni][nj] in up):
                            adj[i][j] = 1
                        if (k == 1) and (tunnel[ni][nj] in down):
                            adj[i][j] = 1
                        if (k == 2) and (tunnel[ni][nj] in left):
                            adj[i][j] = 1
                        if (k == 3) and (tunnel[ni][nj] in right):
                            adj[i][j] = 1
    # print(tunnel)
    print(adj)