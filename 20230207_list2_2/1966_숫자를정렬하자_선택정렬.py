T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(f'#{tc}', *arr)

