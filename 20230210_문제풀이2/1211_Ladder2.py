for tc in range(1, 11):
    N = int(input())
    arr2 = [([0] + list(map(int, input().split())) + [0]) for _ in range(100)]
    start = {}

    for k in range(101):
        arr = [x[:] for x in arr2]
        ''' 같은 의미
        for x in arr2:
            arr = list(x[:])
        '''

        if arr[0][k]:           # START
            i = 0
            j = k

            di = [1, 0, 0]              # 하 우 좌
            dj = [0, 1, -1]

            dir = 0
            count = 0

            while True:

                i += di[dir]
                j += dj[dir]

                if i == 100:
                    start[k] = count
                    break

                arr[i][j] = 0
                count += 1

                if arr[i][j+1]:
                    dir = 1

                elif arr[i][j-1]:
                    dir = 2

                else:
                    dir = 0

    minV = 999
    for x, v in start.items():

        if minV > v:
            minV = v
            minIdx = x
    print(f'#{tc}', minIdx - 1)