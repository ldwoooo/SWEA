def dfs(S, G):
    '''
    길찾는 함수
    S : 출발 노드
    '''

    # 방문배열
    visited = [0] * (V + 1)
    stack = []
    # 출발 노드를 현재 위치로 설정
    location = S
    # 지나온 노드들을 순서대로 기록하기 위해 stack 에 쌓아둠
    stack.append(location)

    while True:
        # 현재 위치가 도착 노드이면 탐색 성공
        if location == G:
            return 1

        # 그렇지 않으면 계속 탐색
        for v in range(V + 1):
            # 길이 존재하고 방문하지 않은 노드이면
            if adj[location][v] == 1 and visited[v] == 0:
                # 방문 리스트 체크
                visited[v] = 1
                # 방문 리스트를 현재위치로
                location = v
                # 현재위치 stack 에 순서대로 쌓아서 기록
                stack.append(location)
                break
        # break 로 빠져나온게 아니면
        # 길이 존재하지 않거나 다음 경로가 방문한 노드이면
        else:
            # stack 에 남아있으면
            if stack:
                # 그 전에 노드로 한 번 돌아가보자
                location = stack.pop()
            # 도착 노드에 도착하지 못했는데 지나온 노드를 다 썼어... 실패
            else:
                # return 0          # 같은 결과
                break
    return 0


# 입력 부분
T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접행렬
    adj = [[0] * (V + 1) for _ in range(V + 1)]

    # 길들을 입력 받고 인접행렬 생성
    for _ in range(E):
        start, to = map(int, input().split())
        adj[start][to] = 1

    # 출발 노드, 도착 노드 입력
    S, G = list(map(int, input().split()))

    print(f'#{tc}', dfs(S, G))
