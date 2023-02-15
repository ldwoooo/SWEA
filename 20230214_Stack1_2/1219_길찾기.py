def dfs(start):
    '''
    길찾기 함수
    :param start: 출발 번호
    '''

    # 방문배열
    visited = [0] * 100

    stack = []

    # 시작 지점을 현재위치(location)로 바꾸고 방문 배열에 체크
    location = start
    visited[location] = 1

    while True:

        # 현재위치가 도착지점이면 1 반환
        if location == 99:
            return 1

        else:
            for v in range(100):
                # 현재위치에서 존재하는 길을 찾는 과정. 길이 존재하고 방문하지 않았다면
                if adj[location][v] == 1 and visited[v] == 0:

                    # 방문 체크
                    visited[v] = 1
                    # 현재위치를 스택에 넣는다(기록한다)
                    stack.append(location)
                    # 방문 위치를 현재위치로 바꿔줌
                    location = v
                    break

            # break를 만나지 않고 나옴
            # 현재 위치에서 존재하는 길이 없는 경우
            else:
                # 지나온 위치들을 기록해논 stack 이 남아있으면
                if stack:
                    # 가장 최근에 지나온 위치로 돌아가서 다시 길 탐색
                    location = stack.pop()
                # 기록해논 위치가 다 떨어지면 다 탐색한거임
                else:
                    break
    return 0


# 입력부분
for tc in range(1, 11):
    _, Bridge = map(int, input().split())
    node = list(map(int, input().split()))

    # 인접행렬 생성
    # 출발 0 ~ 도착 99 이므로 100X100 행렬 생성
    adj = [[0] * 100 for _ in range(100)]

    # 존재하는 길은 1
    for i in range(Bridge):
        adj[node[i * 2]][node[i * 2 + 1]] = 1

    print(f'#{tc}', dfs(0))
