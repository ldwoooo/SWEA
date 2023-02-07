T = int(input())

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0

    for i in range(1 << len(arr)):
        new_arr = []
        for j in range(len(arr)):
            if i & (1 << j):
                new_arr.append(arr[j])

        if len(new_arr) == N and sum(new_arr) == K:
            count += 1

    print(f'#{tc}', count)