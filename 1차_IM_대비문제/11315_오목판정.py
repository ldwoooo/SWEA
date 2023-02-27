def row():
    # 가로검사
    for i in range(N):
        count = 0
        for j in range(N):
            if omok[i][j] == 'o':
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
    return False


def column():
    # 세로검사
    for j in range(N):
        count = 0
        for i in range(N):
            if omok[i][j] == 'o':
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
    return False


def cross():
    # 대각선(\) 검사
    count = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                if omok[i][j] == 'o':
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
    return False


def cross2():
    # 대각선(/) 검사
    count = 0
    for i in range(N):
        for j in range(N):
            if i + j == N - 1:
                if omok[i][j] == 'o':
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
    return False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    omok = [input() for _ in range(N)]

    if row() or column() or cross() or cross2():
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')