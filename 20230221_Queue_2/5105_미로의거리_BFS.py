def bfs(i, j, n):
    # 방문 행렬
    visited = [[0] * n for _ in range(n)]
    queue = [(i, j)]                        # 시작 인덱스 큐에 넣기
    visited[i][j] = 1                       # 방문 행렬에 1 ++

    di = [0, 0, -1, 1]                      # 좌우상하
    dj = [-1, 1, 0, 0]
    while queue:                            # 큐가 빌 때까지
        i, j = queue.pop(0)                 # 시작 인덱스 뽑아서

        for k in range(4):                  # 좌우상하 탐색
            ni = i + di[k]
            nj = j + dj[k]
            # 유효한 인덱스, 벽(1)이 아니고 방문하지 않았으면
            if (0 <= ni < N) and (0 <= nj < N) and (maze[ni][nj] != 1) and (visited[ni][nj] == 0):
                queue.append((ni, nj))      # 큐에 넣고 방문 행렬에 1 ++
                visited[ni][nj] = visited[i][j] + 1

        if maze[i][j] == 3:                 # 도착지에 다다르면 지나온 경로 갯수 반환
            return visited[i][j] - 2        # 문제에서 시작과 도착지는 제외해야 함

    return 0                                # 경로가 없는 경우


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    si = sj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:         # 미로 시작점 찾기
                si, sj = i, j
                break

    print(f'#{tc}', bfs(si, sj, N))

# ----------------------------------------------------------------------------------------------------------------
# 교수님 풀이
def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]  # 인큐 확인배열
    q = [(i, j)]  # 큐 생성, 시작점 인큐
    visited[i][j] = 1  # 시작점 표시
    while q:  # 큐가 비어있지 않으면
        i, j = q.pop(0)
        if maze[i][j] == '3':  # i,j가 도착지인가?
            return visited[i][j] - 2
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and visited[ni][nj] == 0:  # 벽이 아니고, 인큐한 적 없으면
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0  # '3'칸에 못가는 경우


def findStart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j
    return -1, -1  # return 형식 맞추기용


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [input() for _ in range(N)]

    # si = sj = -1
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j]=='2':
    #             si, sj = i, j
    #             break
    #     if si!=-1:
    #         break
    si, sj = findStart(N)

    print(f'#{tc} {bfs(si, sj, N)}')

# ---------------------------------------------------------------------------------------------------------------
# 교수님 풀이 front, rear 이용
def bfs(i, j, N):
    q = [0] * (N * N)
    front = -1
    rear = -1
    visited = [[0] * N for _ in range(N)]
    rear += 1
    q[rear] = (i, j)
    while front != rear:
        front += 1
        i, j = q[front]
        if maze[i][j] == '3':
            return visited[i][j] - 1                        # 여기서는 왜 -1을 해줘야 하지???????????????????
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                rear += 1
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1
    return 0


def findStart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j
    return -1, -1  # return 형식 맞추기용


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [input() for _ in range(N)]

    si, sj = findStart(N)
    print(f'#{tc} {bfs(si, sj, N)}')