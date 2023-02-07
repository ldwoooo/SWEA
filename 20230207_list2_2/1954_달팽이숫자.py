T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    dir = 0
    i = 0
    j = 0

    for k in range(1, N * N + 1):
        matrix[i][j] = k
        ni = i + di[dir]
        nj = j + dj[dir]

        if (0 <= ni < N) and (0 <= nj < N) and (matrix[ni][nj] == 0):
            i = ni
            j = nj

        else:
            dir = (dir + 1) % 4
            i = i + di[dir]
            j = j + dj[dir]

    print(f'#{tc}')
    for x in matrix:
        print(*x)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    dir = 0
    i = 0
    j = 0

    for k in range(1, N * N + 1):
        matrix[i][j] = k
        ni = i + di[dir]
        nj = j + dj[dir]

        if (0 <= ni < N) and (0 <= nj < N) and (matrix[ni][nj] == 0):
            i = ni
            j = nj

        else:
            dir = (dir + 1) % 4
            i = i + di[dir]
            j = j + dj[dir]

    print(f'#{tc}')
    for x in matrix:
        print(*x)
