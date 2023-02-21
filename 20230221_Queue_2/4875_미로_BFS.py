def bfs(si, sj, n):
    # 방문 행렬
    visited = [[0] * n for _ in range(n)]
    queue = [(si, sj)]
    visited[si][sj] = 1

    while queue:
        i, j = queue.pop(0)

        if maze[i][j] == 3:
            return 1

        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:         # 좌우상하
            ni, nj = i + di, j + dj
            if (0 <= ni < n) and (0 <= nj < n) and (maze[ni][nj] != 1) and (visited[ni][nj] == 0):
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발지 찾기
    si = sj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    print(f'#{tc}', bfs(si, sj, N))

