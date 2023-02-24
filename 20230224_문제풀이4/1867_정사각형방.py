T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]              # 상하좌우
    dj = [0, 0, -1, 1]

    ans = 0
    start = N * N
    for i in range(N):
        for j in range(N):
            move = []
            count = 1                                   # 이동하기 전 기존의 방 카운트
            k = 0
            while k < 4:                                # 상하좌우 다 돌때까지
                ni = i + di[k]
                nj = j + dj[k]

                # 유효한 인덱스에 있고 본인 방 기준 상하좌우 방에 적힌 숫자가 1이 클 때
                if (0 <= ni < N) and (0 <= nj < N) and (room[i][j] - room[ni][nj] == -1):
                    move.append(room[i][j])             # 움직인 방들을 넣어줘
                    i, j = ni, nj                       # 움직인 방으로 인덱스를 바꿔주고
                    count += 1                          # 움직인 수만큼 1++
                    k = 0                               # 델타 초기화
                else:
                    k = (k + 1) % 5                     # k = 4가 되면 빠져나올 수 있게 설정

            if move:                                    # 이동을 했다면
                if ans < count:                         # 움직인 방의 수가 최대라면
                    ans = count                         # 움직인 횟수와 움직이기 시작한 방 반환
                    start = move[0]
                elif ans == count:                      # 움직인 방의 수가 같으면
                    ans = count
                    if start > move[0]:                 # 움직이기 시작한 방 중 작은 숫자 반환
                        start = move[0]

    print(f'#{tc}', start, ans)
# --------------------------------------------------------------------------------------------------------
# 교수님 코드
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * (N * N + 1)  # 연속한 숫자 기록
    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and room[ni][nj] - room[i][j] == 1:
                    cnt[room[i][j]] = 1
                    break  # 1큰 경우는 최대 한 개이므로 탐색 중단
    # 연속한 1의 개수 중 가장 긴 경우 찾기, 길이가 같으면 시작 인덱스가 작은 것
    maxIdx = 0
    maxV = 0
    ones = 0
    for i in range(N * N, 0, -1):   # 동일한 경우 작은 숫자를 출력해야하므로 뒤에서부터 탐색함!!! 대박!!
        if cnt[i] == 1:
            ones += 1
            if maxV <= ones:
                maxV = ones
                maxIdx = i
        else:
            ones = 0

    print(f'#{tc} {maxIdx} {maxV + 1}')
