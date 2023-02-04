T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count_arr = []

    for i in range(N):
        count = 0
        for j in arr[i + 1:]:
            if arr[i] > j:
                count += 1
            count_arr.append(count)

    maxV = count_arr[0]

    for k in count_arr:
        if maxV < k:
            maxV = k

    print(f'#{test_case}', maxV)
