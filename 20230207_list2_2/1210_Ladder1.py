for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]


    for k in range(100):
        if arr[99][k] == 2:
            i = 99
            j = k
    
    di = [-1, 0, 0]  # 상, 좌, 우
    dj = [0, -1, 1]
    dir = 0

    while True:
        i += di[dir]
        j += dj[dir]

        if i == 0:
            print(f'#{N}', j)
            break

        arr[i][j] = 0

        if (0 <= i + di[1] < 100) and (0 <= j + dj[1] < 100) and (arr[i + di[1]][j + dj[1]] == 1):
            dir = 1
            
        elif (0 <= i + di[2] < 100) and (0 <= j + dj[2] < 100) and (arr[i + di[2]][j + dj[2]] == 1):
            dir = 2

        elif (0 <= i + di[0] < 100) and (0 <= j + dj[0] < 100) and (arr[i + di[0]][j + dj[0]] == 1):
            dir = 0