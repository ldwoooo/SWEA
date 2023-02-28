def check():
    di = [0, 1, 1, 1]  # 오른쪽, 오른쪽 아래, 아래, 왼쪽 아래
    dj = [1, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            count = 0                               # 초기화 부분의 순서 매우 중요하다!!!!
            k = 0
            if omok[i][j] == 'o':                   # 돌을 만나면 냅다 카운트해주고 현재 위치를 기억해야하기 때문에 a, b에 따로 할당해준다.
                count += 1
                a, b = i, j
                while k < 4:                        # 델타 방향을 다 돌면 while 문 종료
                    ni, nj = a + di[k], b + dj[k]
                    if (0 <= ni < N) and (0 <= nj < N) and omok[ni][nj] == 'o':     # 새로운 방향이 유효한 인덱스이고 돌이 있으면
                        a, b = ni, nj
                        count += 1
                        if count == 5:              # 5개 연속 되면 YES 반환하고 함수 종료
                            return 'YES'
                    else:
                        a, b = i, j                 # 현재 위치로 다시 돌아가
                        k += 1                      # 델타 방향 바꿔주고
                        count = 1
    return 'NO'


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    omok = [input() for _ in range(N)]

    print(f'#{tc}', end=' ')
    print(check())
