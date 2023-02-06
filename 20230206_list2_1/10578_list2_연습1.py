T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # i행, j열로 움직일 수 있는 범위 설정(상하좌우)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    S = []

    for i in range(N):
        for j in range(N):
            for k in range(4):

                # 상하좌우
                ni = i + di[k]
                nj = j + dj[k]

                # 유효한 인덱스이면
                if 0 <= ni < N and 0 <= nj < N:

                    # 조건문을 통해 절댓값으로 차이 구하기
                    if arr[i][j] > arr[ni][nj]:
                        a = arr[i][j] - arr[ni][nj]
                        S.append(a)

                    else:
                        b = arr[ni][nj] - arr[i][j]
                        S.append(b)
    # 총합
    y = 0
    for x in S:
        y += x
    print(f'#{tc}', y)
