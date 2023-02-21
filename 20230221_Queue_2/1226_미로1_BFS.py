def bfs(i, j, n):
    # 방문행렬
    visited = [[0] * n for _ in range(n)]
    queue = [(i, j)]
    visited[i][j] = 1

    while queue:
        i, j = queue.pop(0)

        if maze[i][j] == '3':
            return 1

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            if (0 <= ni < n) and (0 <= nj < n) and (maze[ni][nj] != '1') and (visited[ni][nj] == 0):
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


for tc in range(1, 11):
    t = input()
    maze = [input() for _ in range(16)]

    print(f'#{tc}', bfs(1, 1, 16))
