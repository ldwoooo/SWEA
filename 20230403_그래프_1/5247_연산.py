# 큐덱을 쓰면 시간 줄일 수 있음
# from collections import deque

# def bfs(n, m):

#     q = deque([n])
#     visited[n] = 1

#     t = q.popleft()
#     while t != m:

#         for rlt in (t + 1, t - 1, t * 2, t - 10):
#             if 1 <= rlt <= 1000000 and visited[rlt] == 0:
#                 visited[rlt] = visited[t] + 1
#                 q.append(rlt)

#         t = q.popleft()

def bfs(n, m):
    

    q = [n]                         # 큐를 만들고
    visited[n] = 1                  # 방문 체크해주고

    t = q.pop(0)                    # 시작 값을 먼저 꺼내주고
    while t != m:

        for rlt in (t + 1, t - 1, t * 2, t - 10):               # 갈 수 있는 가짓수를 반복하고
            if 1 <= rlt <= 1000000 and visited[rlt] == 0:       # 범위 내에 있으며 방문하지 않았다면
                visited[rlt] = visited[t] + 1                   # 누적 합으로 횟수를 세주고
                q.append(rlt)                                   # 그 값을 다시 큐에 넣어줘 반복한다

        # 같은 의미
        # rlt1 = t + 1
        # rlt2 = t - 1
        # rlt3 = t * 2
        # rlt4 = t - 10
        #
        # if 1 <= rlt1 <= 1000000 and visited[rlt1] == 0:
        #     visited[rlt1] = visited[t] + 1
        #     q.append(rlt1)
        #
        # if 1 <= rlt2 <= 1000000 and visited[rlt2] == 0:
        #     visited[rlt2] = visited[t] + 1
        #     q.append(rlt2)
        #
        # if 1 <= rlt3 <= 1000000 and visited[rlt3] == 0:
        #     visited[rlt3] = visited[t] + 1
        #     q.append(rlt3)
        #
        # if 1 <= rlt4 <= 1000000 and visited[rlt4] == 0:
        #     visited[rlt4] = visited[t] + 1
        #     q.append(rlt4)

        t = q.pop(0)                                            # 넣어준 거 다시 앞에서 부터 뺴


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 2000000                 # 방문 행렬
    cnt = 0
    bfs(N, M)
    # print(visited)
    print(f'#{tc}', visited[M] - 1)         