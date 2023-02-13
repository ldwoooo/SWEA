T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    for i in range(len(arr)):
        for j in range(len(arr) - (M - 1)):                     # 찾아야 하는 회문의 길이
            for k in range((M // 2) + 1):
                if arr[i][j + k] != arr[i][j + (M - 1) - k]:
                    break
                else:
                    if k == (M - 1) // 2:
                        result = arr[i][j: j + M]

                        print(f'#{tc}', end=' ')
                        for x in result:
                            print(x, end='')
                        print()

    for i in range(len(arr)):
        for j in range(len(arr) - (M - 1)):
            for k in range((M // 2) + 1):
                if arr[j + k][i] != arr[j + (M - 1) - k][i]:
                    break
                else:
                    if k == (M - 1) // 2:
                        result = [arr[l][i] for l in range(j, j + M)]

                        print(f'#{tc}', end=' ')
                        for x in result:
                            print(x, end='')
                        print()
