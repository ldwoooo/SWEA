def bfs(s, g, v):

    # 방문행렬
    visited = [0] * (v + 1)
    queue = [s]                                 # 큐에 출발지 넣어주고
    visited[s] = 1                              # 방문행렬에도 1 ++
    # print(queue, end = ' ')
    # print(visited)
    while queue:                                # 큐가 빌 때까지
        t = queue.pop(0)                        # 시작점 노드를 빼서

        for i in adj[t]:                        # 시작점 노드의 인접 노드를 찾아서
            if visited[i] == 0:                 # 방문하지 않았으면
                queue.append(i)                 # 큐에 넣어줘
                visited[i] = visited[t] + 1     # 방문행렬에 1 ++
            # print(queue, end = ' ')
            # print(visited)
    if visited[g] == 0:                         # 도착지점에 닿지 않았으면 실패
        return 0
    else:
        return visited[g] - 1


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접행렬
    adj = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, to = map(int, input().split())
        adj[start].append(to)
        adj[to].append(start)
    # print(adj)

    S, G = map(int, input().split())

    print(f'#{tc}', bfs(S, G, V))

