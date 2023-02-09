def palindrome(arr):

    i = 0
    j = 0
    k = M - 1
    if N == M:
        while i < N and j < M // 2:
            if arr[i][j] == arr[i][k]:
                j += 1
                k -= 1

            else:
                i += 1

        if j == M // 2:
            return arr[i]
        else:
            return change(arr)
    else:
        while i < N and k > 0:

            if arr[i][j] == arr[i][j + k]:
                j += 1
                k -= 2
            else:
                j += 1
                k = M - 1
                if j >= N - M + 1:
                    i += 1
                    j = 0

        if k == 0:
            return arr[i][j-(M//2): j-(M//2) + M]
        else:
            return change(arr)


def change(arr):
    na = [['0'] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            na[i][j] = arr[j][i]
    return palindrome(na)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr2 = [list(map(str, input())) for _ in range(N)]

    print(f'#{tc}', end=' ')
    for x in palindrome(arr2):
        print(x, end='')
    print()

