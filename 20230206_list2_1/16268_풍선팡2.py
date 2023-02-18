T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]      # 우하죄상
    dj = [1, 0, -1, 0]

    maxV = 0
    for i in range(N):
        for j in range(M):

            flower = 0
            flower += arr[i][j]             # 터트릴 풍선 꽃가루 더해주기
            for k in range(4):

                ni = i + di[k]              # 우하상좌 순서대로 돌자
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < M:     # 행렬 안에 존재할 때
                    flower += arr[ni][nj]           # 꽃가루 더해주기

            if maxV < flower:               # 꽃가루 최댓값 구하기
                maxV = flower
                
    print(f'#{tc}', maxV)
