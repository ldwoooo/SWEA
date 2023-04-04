def f(N):
    INF = 10000
    D = [[INF] * N for _ in range(N)]       # 인피니티 값으로 가중치 배열 생성
    D[0][0] = 0                             # 시작점
    U = [[0] * N for _ in range(N)]         # 노드 확정 배열 방문 배열
    U[0][0] = 1                             # 시작점 확정하고 시작

    for _ in range(N * N - 1):              # 도착점을 제외하고 돌아라
        minV = INF
        wi, wj = 0, 0
        for i in range(N):                  # 2차배열 돌면서
            for j in range(N):
                if U[i][j] == 0 and minV > D[i][j]:     # 방문하지 않고 가중치가 최소값보다 작으면
                    minV = D[i][j]                      # 최소값 갱신
                    wi, wj = i, j                       # 위치도 이동시켜
        U[wi][wj] = 1                                   # 방문 체크 까먹지 말고

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:       # 델타로 움직이면서
            ni, nj = wi + di, wj + dj   
            if 0 <= ni < N and 0 <= nj < N and U[ni][nj] == 0:      # 유효한 인덱스에 있고 방문하지 않았으면
                cost = 1 + max(0, H[ni][nj] - H[wi][wj])            # 연료 측정(이동연료 1 + 높이 차이)하고 
                D[ni][nj] = min(D[ni][nj], D[wi][wj] + cost)        # 기존 위치에 있던 가중치 값이랑 전에서 연료 측정해서 온 값이랑 최소 비교
    return D[N-1][N-1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', f(N))

# BFS 이용
def bfs(N):
    INF = 10000
    D = [[INF] * N for _ in range(N)]
    D[0][0] = 0
    q = [[0, 0]]
    while q:
        i, j = q.pop(0)
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and D[ni][nj] > D[i][j] + (1 + max(0, H[ni][nj] - H[i][j])):
                D[ni][nj] = D[i][j] + (1 + max(0, H[ni][nj] - H[i][j]))
                q.append([ni, nj])
    return D[N - 1][N - 1]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', bfs(N))
