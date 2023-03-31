def backtracking(i, n, cost):
    '''
    :param i: 행. 상품 인덱스
    :param n: 행의 마지막 인덱스. 상품의 개수
    :param cost: 누적 합의 값. 상품의 비용 누적합
    '''
    global minV

    if i == n:                      # 끝까지 도달 했으면 최소 비용 비교
        minV = min(minV, cost)
        return

    if minV < cost:                 # 가지치기. 이미 최소 값보다 누적합이 크면 멈춰
        return

    for j in range(n):              # 열 반복
        if visited[j] == 0:         # 방문하지 않았으면
            visited[j] = 1          # 방문하고
            backtracking(i + 1, n, cost + V[i][j])      # 행 바꿔서 다시 돌아봐. 방문한 자리 누적합해주고
            visited[j] = 0          # 끝까지 돌면 열 바꿔서 반복해야하니까 돌아와. 방문배열은 초기화 해주고


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    minV = 99 * N
    visited = [0] * N               # 방문배열
    backtracking(0, N, 0)
    print(f'#{tc}', minV)
