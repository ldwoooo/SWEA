def bfs(s):
    global maxIdx
    # 방문행렬
    visited = [0] * 101                         # 초기 설정
    q = [s]
    visited[s] = 1

    while q:
        ns = q.pop(0)

        for n in adj[ns]:                       # 다음 행선지의 연락망 탐색
            if visited[n] == 0:                 # 다음 연락망을 연락한 적이 없으면
                q.append(n)                     # 연락해라
                visited[n] = visited[ns] + 1    # 누적 합

    for j in range(len(visited)):               # visited 최대값의 인덱스는 노드임을 활용
        if visited[maxIdx] <= visited[j]:       # 가장 늦게 연락 받은 횟수
            if maxIdx < j:                      # 그 중 큰 숫자
                maxIdx = j

    return maxIdx
''' 혜진님 코드
def bfs(s):
    q = []
    visited = [0] * 101
    q.append(s)             # 초기 설정
    visited[s] = 1
    ans = 0
    while len(q):
        v = q.pop(0)        #  v :현재
        # 조건 제일 늦게 나타난 노드 , 그 중 가장 큰 숫자
        if visited[v] > visited[ans] or (visited[ans] == visited[v] and\
            ans < v):
            ans = v
 
        for n in adj[v]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = visited[v] + 1         # 누적 합
'''

for tc in range(1, 11):
    N, S = map(int, input().split())
    contact = list(map(int, input().split()))

    # 인접 행렬
    adj = [[] for _ in range(101)]
    for i in range(N // 2):
        f = contact[i * 2]
        t = contact[i * 2 + 1]

        if t not in adj[f]:                     # 겹치는 노선 정리
            adj[f].append(t)

    maxIdx = 0
    print(f'#{tc}', bfs(S))
