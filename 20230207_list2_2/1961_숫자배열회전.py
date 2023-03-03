def rotate(arr, na) -> object:

    for i in range(N):
        for j in range(N):
            na[i][j] = arr[N - 1 - j][i]
    return na


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    na_90 = [[0] * N for _ in range(N)]
    na_180 = [[0] * N for _ in range(N)]
    na_270 = [[0] * N for _ in range(N)]

    print(f'#{tc}')
    for i in range(N):
        print(*rotate(nums, na_90)[i], sep='', end=' ')
        print(*rotate(na_90, na_180)[i], sep='', end=' ')
        print(*rotate(na_180, na_270)[i], sep='', end=' ')
        print()
