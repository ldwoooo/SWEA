def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())        # V 마지막 노드번호, E 간선의 개수

    # 1. makeset
    rep = [i for i in range(V + 1)]
    graph = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())       # n1, n2 간선의 양 끝 노드, w 가중치
        graph.append([n1, n2, w])

    # 2. 가중치 오름차순 정렬
    graph.sort(key=lambda x:x[2])
    # print(graph)

    # 3. 가중치가 가장 낮은 간선부터 선택
    N = V + 1                                   # 노드의 개수
    cnt = 0
    s = 0
    for i in range(E):
        v1, v2, w = graph[i][0], graph[i][1], graph[i][2]   # 가중치가 작은 값부터 담아주고

        if find_set(v1) != find_set(v2):        # 사이클이 생기지 않는 경우라면
            s += w                              # 가중치 누적해주고
            cnt += 1                            # 간선 갯수 세어줘
            union(v1, v2)                       # 간선 그어주고
            if cnt == N - 1:
                break
    print(f'#{tc}', s)

    # 같은 풀이. BUT cnt가 다 차면 빠져 나오게끔 위의 코드와 같이 해주는 것이 더 좋다!!

    #  while cnt != N - 1:                 # 트리가 완성될 때까지
    #
    #         for i in range(E):
    #             v1, v2, w = graph[i][0], graph[i][1], graph[i][2]   # 가중치가 작은 값부터 담아주고
    #
    #             if find_set(v1) != find_set(v2):        # 사이클이 생기지 않는 경우라면
    #                 s += w                              # 가중치 누적해주고
    #                 cnt += 1                            # 간선 갯수 세어줘
    #                 union(v1, v2)                       # 간선 그어주고
    #     print(f'#{tc}', s)

