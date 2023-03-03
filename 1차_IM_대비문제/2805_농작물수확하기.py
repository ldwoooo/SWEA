def bfs(i, j):
    visited = [[0] * 50 for _ in range(50)]                                     # 방문 행렬
    visited[i][j] = 1                                                           # 초기 방문, 큐, 농작물 가치 설정
    q = [(i, j)]
    ans = worth[i][j]
    while True:
        a, b = q.pop(0)
        # 사실 순서를 잘 따라가면 오른쪽이 제일 먼저 pop 되므로 가장 오른쪽인 b == N-1 조건만 있어도 됨
        if (a == 0) or (a == N - 1) or (b == 0) or (b == N - 1):
            break
        for di, dj in [[0, 1], [0, -1], [-1, 0], [1, 0]]:                       # 우좌상하
            ni, nj = a + di, b + dj
            if (0 <= ni < N) and (0 <= nj < N) and (visited[ni][nj] == 0):      # 유효한 인덱스, 방문하지 않았으면
                ans += worth[ni][nj]                                            # 가치 누적 합
                visited[ni][nj] = 1                                             # 방문 체크
                q.append((ni, nj))                                              # 큐에 새로운 위치 넣어주기

    return ans


T = int(input())

for tc in range(1, T + 1):                                  # 입력
    N = int(input())
    worth = [list(map(int, input())) for _ in range(N)]

    i = j = N // 2
    print(f'#{tc}', bfs(i, j))

# ---------------------------------------------------------------------------------------------------------------------
# 성구 코드
# 아마 농작물이 없는 부분을 제거 한다고 생각하면 편할 듯
for test_case in range(1, int(input())+1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    c = N//2
    benefit = 0
    for i in range(N):
        for j in range(abs(c-i), N-abs(c-i)):   
            benefit += int(farm[i][j])  
    print(f'#{test_case} {benefit}')
