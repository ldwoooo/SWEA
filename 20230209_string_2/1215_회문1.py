for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0

    for i in range(len(arr)):
        for j in range(len(arr) - (N - 1)):                     # 찾아야 하는 회문의 길이
            for k in range((N // 2) + 1):
                if arr[i][j + k] != arr[i][j + (N - 1) - k]:
                    break
                else:
                    if k == (N - 1) // 2:
                        count += 1

    for i in range(len(arr)):
        for j in range(len(arr) - (N - 1)):
            for k in range((N // 2) + 1):
                if arr[j + k][i] != arr[j + (N - 1) - k][i]:
                    break
                else:
                    if k == (N - 1) // 2:
                        count += 1
    print(f'#{tc}', count)
