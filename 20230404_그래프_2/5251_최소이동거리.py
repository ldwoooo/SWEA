def dijktra(s, n):
    U = [0] * (n + 1)                   # 기본 세팅
    U[s] = 1

    for i in range(n + 1):              # 시작점 기준 갈 수 있는 노드 복사
        D[i] = adj[s][i]

    for _ in range(n + 1):              # 간선 수만큼 돌면서 체크
        minV = INF
        k = 0
        for a in range(n + 1):
            if U[a] == 0 and minV > D[a]:   # 방문하지 않았고 가중치가 최소이면
                minV = D[a]                 # 최소 가중치를 주고
                k = a                       # 이동시킴
        U[k] = 1                    # 방문 체크
                
        for b in range(n + 1):
            if 0 < adj[k][b] < INF:         # 이동시킨 노드의 인접 노드 탐색
                D[b] = min(D[b], D[k] + adj[k][b])      # 그냥 가는거랑 이동시킨 노드를 거쳐서 가는 거랑 최소 가중치 계산



T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())    # N 마지막 지점(가야할 지점), E 간선 수

    INF = 11
    adj = [[INF] * (N + 1) for _ in range(N + 1)]   # 인접행렬 인피니티 값으로 만들고
    for i in range(N + 1):              # 본인 자신으로 돌아오는 경우는 0
        adj[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w                   # 시작점에서 마지막점 가중치 대입

    # print(adj)
    D = [0] * (N + 1)
    dijktra(0, N)
    print(f'#{tc}', D[N])