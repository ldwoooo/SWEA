T = int(input())

for tc in range(1, T + 1):                                              # 입력
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]                                                  # 상하좌우
    dj = [0, 0, -1, 1]

    maxV = 0
    for i in range(N):                                                  # 2차 배열 탐색
        for j in range(M):
            flower = 0
            flower += balloon[i][j]                                     # 본인 자리 꽃가루 더해줘
            for k in range(4):                                          # 델타 탐색
                ni = i + di[k]
                nj = j + dj[k]
                if (0 <= ni < N) and (0 <= nj < M):                     # 유효한 인덱스에 있으면
                    flower += balloon[ni][nj]                           # 꽃가루 더해줘

            if maxV < flower:                           # 상하좌우를 다 돌고 최대 꽃가루 구하기
                maxV = flower

    print(f'#{tc}', maxV)
 