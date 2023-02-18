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
                
                a, b = i, j                     # 아랫줄 터트린 풍선 제자리를 유지해야하기 때문에 i, j를 a, b에 잠시 담아둔다 
                for _ in range(arr[i][j]):      # 터트린 풍선의 꽃가루 수만큼 반복
                    ni = a + di[k]              # 우하상좌 순서대로 돌자
                    nj = b + dj[k]

                    if 0 <= ni < N and 0 <= nj < M:     # 행렬 안에 존재할 때
                        flower += arr[ni][nj]           # 꽃가루 더해주기
                        a, b = ni, nj           # 꽃가루 수 만큼 더 가기 위해 자리 이동 

            if maxV < flower:               # 꽃가루 최댓값 구하기
                maxV = flower

    print(f'#{tc}', maxV)
