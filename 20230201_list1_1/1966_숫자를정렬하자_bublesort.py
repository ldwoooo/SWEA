T = int(input())

for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for j in range(N-1, 0, -1):
        for k in range(0, j):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]

    print(f'#{i}', *arr)
